from rest_framework.exceptions import ValidationError


class SimultaneousSelection:
    """Валидация на совместный выбор 'связанной привычки' и 'вознаграждения'."""

    def __init__(self, connection_habit, reward):
        self.field_1 = connection_habit
        self.field_2 = reward

    def __call__(self, habit):
        if habit.get(self.field_1) and habit.get(self.field_2):
            raise ValidationError(
                "Нельзя одновременно выбирать связанную привычку и вознаграждение"
            )


def validate_duration(duration):
    """ В связанные привычки могут попасть только - приятные."""
    if duration and duration > 120:
        raise ValidationError("время выполнения не должно превышать 120 секунд")


class ConnectionHabitCheck:

    def __call__(self, habit):
        if habit.get("connection_habit"):
            if not habit.get("connection_habit").nice_habit_bool:
                raise ValidationError(
                    "В связанные привычки могут попасть только - приятные..."
                )


class NiceHabitRewardCheck:

    def __call__(self, habit):
        if habit.get("nice_habit_bool"):
            if habit.get("reward") or habit.get("connection_habit"):
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки"
                )