from django.db import models

from config.settings import AUTH_USER_MODEL
import datetime

NULLABLE = {"null": True, "blank": True}


class Habit(models.Model):
    """Модель привычки."""

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        **NULLABLE,
    )
    place = models.CharField(
        max_length=150, verbose_name="Место выполнения", **NULLABLE
    )
    start_time = models.TimeField(
        default=datetime.datetime.now().time(),
        verbose_name="Время начала выполнения",
        **NULLABLE,
    )
    action = models.CharField(max_length=150, verbose_name="Действие")
    nice_habit_bool = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    connection_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="Связанная привычка", **NULLABLE
    )
    periodicity = models.IntegerField(
        default=3, verbose_name="периодичность напоминания в днях"
    )
    check_periodicity = models.IntegerField(
        default=0, verbose_name="проверка периодичности"
    )
    reward = models.CharField(max_length=150, verbose_name="Вознаграждение", **NULLABLE)
    duration = models.TimeField(verbose_name="Продолжительность выполнения", **NULLABLE)
    published_bool = models.BooleanField(
        default=True, verbose_name="Признак публичности"
    )

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
