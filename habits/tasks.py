import datetime
from habits.services import send_telegram_message
from celery import shared_task

from habits.models import Habit
from users.models import User


@shared_task
def tg_message():
    users = User.objects.all()

    for user in users:
        habits = Habit.objects.filter(owner=user)
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
