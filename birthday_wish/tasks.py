from celery import shared_task
from .models import Customer


@shared_task(name="send_birthday_wish_mail")
def send_birthday_wish_mail():
    print(Customer.objects.all())
    return "Hello"