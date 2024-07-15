from rest_framework.viewsets import generics

from habits.models import Habit
from habits.paginations import HabitsPagination
from habits.serializers import HabitSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    """ Создание привычки. """
    serializer_class = HabitSerializer

    def perform_create(self, serializer):  # функция автора с его привычкой
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitsListAPIView(generics.ListAPIView):
    """ Список привычек. """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPagination


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр одной привычки. """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование привычки. """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки. """
    queryset = Habit.objects.all()