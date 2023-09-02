# Overview
The Automatic Birthday Wish Mailer is a Python-based web application built using Django Rest Framework (DRF), Celery, and Redis. It allows you to schedule and send automatic email wishes for birthdays. 

## Features
- User-friendly web API interface and Django Admin interface to insert Customer Informations.
- Asynchronous email sending using Celery to ensure performance and scalability.
- Supports various scheduling options (daily, weekly, monthly) for wishes using django admin interface without changing the code.
- Integrated Redis for task queue management.

# Prerequisites
Before getting started, make sure you have the following prerequisites:

- Python 3.10 or above installed on your system.
- Django and other required packages installed (see requirements.txt).
- Docker for running the project.
- Docker is used for flexibility through all Operating system. like windows does not support Redis officially. Docker can overcome this kind of issue.

# Installation
Clone the repository:

git clone https://github.com/tasinkhan/Automatic-birthday-wishing-through-email.git

navigate to the folder and run docker-compose file:
- docker-compose up --build -d 

- docker-compose up --build (if want to see the logs without detached mode)

This command will run django, redis, celery worker, celery beat in separate containers.

- go to http:127.0.0.1:8000/customer/ to see the list of the customers or to insert a new customer.

- go to http:127.0.0.1:8000/customer/{id}/ to see details of a customer or edit the informations of a customer.

- go to http:127.0.0.1:8000/admin/ to access the django admin interface.

- login with username:admin, password:admin.

- click on 'Periodic tasks' under 'PERIODIC TASKS' then select 'send_autmomatic_birthday_wish_mail' > Crontab Schedule> then choose which scheduler you want to use. By default we are using midnight(12 am(0 0 * * *  )) to execute the task. But you can select every minute interval(* * * * *) to execute the task and check the periodic task easily.

# About the celery beat DatabaseSchduler
- We are using celery beat to schedule the task at every midnight. 

- Using celery beat database scheduler gives us the flexibility to change schedule using django admin interface so we don't have to hardcode the schedule interval.