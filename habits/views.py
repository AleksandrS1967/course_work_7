from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import generics

from habits.models import Habit
from habits.paginations import HabitsPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    """Создание привычки."""

    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):  # функция автора с его привычкой
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user)


class HabitsPublicListAPIView(generics.ListAPIView):
    """Список публичных привычек."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(published_bool=True)
    pagination_class = HabitsPagination


class HabitsListAPIView(generics.ListAPIView):
    """Список привычек пользователя."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPagination

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user)


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр одной привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки."""

    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
