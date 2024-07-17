from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    """Модель пользователя."""

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )

    phone = models.CharField(
        max_length=35, verbose_name="Телефон", help_text="Укажите телефон", **NULLABLE
    )
    city = models.CharField(max_length=150, verbose_name="Город", **NULLABLE)
    last_login = models.DateTimeField(
        auto_now=True, verbose_name="Время последнего посещения", **NULLABLE
    )
    tg_chat_id = models.CharField(
        max_length=100,
        verbose_name="Телеграм chat-id",
        help_text="Укажите телеграм chat-id",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
