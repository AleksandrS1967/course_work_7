from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitsCreateAPIView,
    HabitsDestroyAPIView,
    HabitsListAPIView,
    HabitsRetrieveAPIView,
    HabitsUpdateAPIView,
    HabitsPublicListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habit/create/", HabitsCreateAPIView.as_view(), name="habit_create"),
    path("habits/", HabitsListAPIView.as_view(), name="habits_list"),
    path("habits/public/", HabitsPublicListAPIView.as_view(), name="habits_list"),
    path("habit/<int:pk>/", HabitsRetrieveAPIView.as_view(), name="habit_get"),
    path("habit/update/<int:pk>/", HabitsUpdateAPIView.as_view(), name="habit_update"),
    path("habit/delete/<int:pk>/", HabitsDestroyAPIView.as_view(), name="habit_delete"),
]
