from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation_email(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        'your_email@example.com',  # Use your sender email
        [recipient_email],
        fail_silently=False,
    )

@shared_task
def send_booking_email(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        'your_email@example.com',  # Replace with your configured sender
        [recipient_email],
        fail_silently=False,
    )
