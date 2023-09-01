from automated_birthday_wishing.celery import test

result = test.delay()
print(result)