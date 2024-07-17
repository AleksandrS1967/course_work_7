import datetime
from habits.services import send_telegram_message
import pytz
from celery import shared_task
from django.core.mail import send_mail

from habits.models import Habit
from users.models import User

zone = pytz.timezone("Europe/Moscow")


@shared_task
def tg_message():
    #  print("1111111111111111111111111111111111111")
    users = User.objects.all()
    habits = Habit.objects.all()
    current_time = datetime.datetime.now().time()

    for user in users:
        for habit in habits:
            if habit.owner == user:
                chat_id = user.tg_chat_id
                if chat_id:
                    habit_time = habit.start_time
                    if habit_time:
                        periodicity = habit.periodicity
                        check_periodicity_ = habit.check_periodicity
                        check_periodicity_ += 1
                        habit.check_periodicity = check_periodicity_
                        habit.save()
                        if habit.check_periodicity == periodicity:
                            habit.check_periodicity = 0
                            habit.save()
                            send_telegram_message(
                                chat_id, f"Пора выполнить привычку:{habit}"
                            )
