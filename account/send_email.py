from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_confirmation_email(email, code):
    activation_url = f'http://127.0.0.1:8000/api/account/activate/?u={code}'
    context = {'activation_url': activation_url}
    subject = 'Здравствуйте, активируйте ваш аккаунт!'
    html_message = render_to_string('account/activate.html', context)
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        'esenkackynbaev6@gmail.com',
        [email],
        html_message=html_message,
        fail_silently=False,
    )


def send_confirmation_password(email, code):
    activation_url = f'http://127.0.0.1:8000/api/account/reset-password/confirm/?user_id={code}'
    context = {'activation_url': activation_url}
    subject = 'Подтвердите изменение пароля '
    html_message = render_to_string('account/new_password.html', context)
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        'esenkackynbaev6@gmail.com',
        [email],
        html_message=html_message,
        fail_silently=True,
    )
