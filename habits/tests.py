from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тесты на CRUD привычек"""

    def setUp(self):
        self.user = User.objects.create(email="tedt@tru.ru")
        self.good_habit = Habit.objects.create(
            action="Полезная привычка",
            duration=120,
            published_bool=True,
            periodicity=3,
            owner=self.user,
        )
        self.nice_habit = Habit.objects.create(
            action="Приятная привычка",
            duration=120,
            published_bool=True,
            periodicity=3,
            nice_habit_bool=True,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_good_habit_retrieve(self):
        url = reverse("habits:habit_get", args=(self.good_habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.good_habit.action)
        self.assertEqual(data.get("owner"), 2)
        self.assertEqual(data.get("duration"), self.good_habit.duration)
        self.assertEqual(data.get("periodicity"), self.good_habit.periodicity)
        self.assertEqual(data.get("published_bool"),
                         self.good_habit.published_bool)

    def test_nice_habit_retrieve(self):
        url = reverse("habits:habit_get", args=(self.nice_habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"),
                         self.nice_habit.action)
        self.assertEqual(data.get("nice_habit_bool"),
                         self.nice_habit.nice_habit_bool)

    def test_good_habit_update(self):
        """Тестирование редактирования."""
        url = reverse("habits:habit_update", args=(self.good_habit.pk,))
        data = {
            "action": "test",
            "duration": 100,
        }
        response = self.client.patch(url, data)
        data_ = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data_.get("action"), "test")
        self.assertEqual(data_.get("duration"), 100)

    def test_good_habit_delete(self):
        """Тестирование удаления."""
        url = reverse("habits:habit_delete", args=(self.good_habit.pk,))
        url_ = reverse("habits:habit_delete", args=(self.nice_habit.pk,))
        response = self.client.delete(url)
        self.client.delete(url_)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
