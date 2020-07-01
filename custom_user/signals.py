from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from . import models as user_models


@receiver(post_save, sender=user_models.RegistrationToken)
def post_save_email_send(sender, **kwargs):
    user = sender.user
    token = sender.token
    subject = 'Добро пожаловать на сайт, {0}'
    html_content = render_to_string('emails/registration_template.html',
                                    {'context': {'token': token}})
    plain_content = strip_tags(html_content)
    from_email = 'placeholder'
    to_email = user.email
    return send_mail(subject, plain_content, from_email, [to_email], html_message=html_content)
