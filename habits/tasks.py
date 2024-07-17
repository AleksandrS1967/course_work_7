import datetime

import pytz
from celery import shared_task
from django.core.mail import send_mail

from habits.models import Habit
from users.models import User

zone = pytz.timezone('Europe/Moscow')


@shared_task
def tg_message():
    print('1111111111111111111111111111111111111')