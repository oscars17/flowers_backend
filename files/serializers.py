from rest_framework.serializers import ModelSerializer
from . import models


class HeaderImageSerializer(ModelSerializer):
    class Meta:
        model = models.HeaderImage
        fields = '__all__'
