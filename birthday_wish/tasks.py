from celery import shared_task
from .models import Customer
from datetime import datetime
from .send_email import SendEmail


@shared_task(name="send_birthday_wish_mail")
def send_birthday_wish_mail():
    current_month = datetime.now().month
    current_date = datetime.now().day
    print("Month", current_month)
    print("Date", current_date)
    # print(Customer.objects.filter(birth_date__month = current_month, birth_date__day = current_date))
    customer_queryset = Customer.objects.filter(birth_date__month = current_month, birth_date__day = current_date)
    for customer in customer_queryset:
        email_handler = SendEmail()
        email_handler.send_mail(name=customer.get_full_name, email=customer.email)
        # print(customer.email)
    return "Email sent successfully"