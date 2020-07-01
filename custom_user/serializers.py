from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify
from custom_user.models import (CustomUser,
                                RegistrationToken
                                )
import re


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=255)
    password_1 = serializers.CharField()
    password_2 = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super(SignUpSerializer, self).__init__(*args, **kwargs)
        error_list = []
        try:
            self.fields['username'].error_messages['blank'] = 'Поле не может быть пустым'
        except KeyError:
            error_list.append("Запрос должен содержать поле 'username'")
        try:
            self.fields['email'].error_messages.update({'blank': 'Поле не может быть пустым',
                                                        'invalid': 'Неверный формат электронной почты'}
                                                        )
        except KeyError:
            error_list.append("Запрос должен содержать поле 'email'")
        try:
            self.fields['password_1'].error_messages['blank'] = 'Поле не может быть пустым'
        except KeyError:
            error_list.append("Запрос должен содержать поле 'password_1'")
        try:
            self.fields['password_2'].error_messages['blank'] = 'Поле не может быть пустым'
        except KeyError:
            error_list.append("Запрос должен содержать поле 'password_2'")
        if len(error_list) != 0:
            raise serializers.ValidationError(' '.join(error_list))

    def validate_username(self, value):
        if len(value) > 10:
            raise serializers.ValidationError('Никнейм не может быть длинее десяти символов')
        elif len(value) < 3:
            raise serializers.ValidationError('Никнейм должен состоять минимум из трех символов')
        if re.match('[a-zA-Z0-9]+', value) is None:
            raise serializers.ValidationError('Имя может содержать только буквы и числа')
        try:
            slug = slugify(value)
            CustomUser.objects.get(slug=slug)
            raise serializers.ValidationError('Имя пользователя занято')
        except ObjectDoesNotExist:
            pass
        return value

    def validate_email(self, value):
        try:
            CustomUser.objects.get(email=value)
            raise serializers.ValidationError('Электронная почта используется '
                                              'другим пользователем')
        except ObjectDoesNotExist:
            pass
        return value

    def validate_password_1(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Пароль должен состоять минимум из восьми символов')
        return value

    def create(self, validated_data):
        new_user = CustomUser()
        new_user.username = validated_data['username']
        new_user.password = validated_data['password']
        new_user.email = validated_data['email']
        new_user.set_password(validated_data['password_1'])
        new_user.save()
        registration_token = RegistrationToken()
        registration_token.user = new_user
        registration_token.save()
        return new_user


class AuthorizationUser(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('slug', 'id', 'username', )
