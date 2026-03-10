from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """Создание и полное обновление (PUT). Валидация: name ≥ 2, age 16–60, email, course 1–6."""
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email', 'course']

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Имя должно быть не короче 2 символов.')
        return value

    def validate_age(self, value):
        if value < 16 or value > 60:
            raise serializers.ValidationError('Возраст должен быть от 16 до 60.')
        return value

    def validate_course(self, value):
        if value < 1 or value > 6:
            raise serializers.ValidationError('Курс должен быть от 1 до 6.')
        return value


class StudentPartialSerializer(serializers.ModelSerializer):
    """Частичное обновление (PATCH) — все поля опциональны, с той же валидацией."""
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email', 'course']
        extra_kwargs = {
            'name': {'required': False, 'min_length': 2},
            'age': {'required': False, 'min_value': 16, 'max_value': 60},
            'email': {'required': False},
            'course': {'required': False, 'min_value': 1, 'max_value': 6},
        }

    def validate_name(self, value):
        if value is not None and len(value) < 2:
            raise serializers.ValidationError('Имя должно быть не короче 2 символов.')
        return value

    def validate_age(self, value):
        if value is not None and (value < 16 or value > 60):
            raise serializers.ValidationError('Возраст должен быть от 16 до 60.')
        return value

    def validate_course(self, value):
        if value is not None and (value < 1 or value > 6):
            raise serializers.ValidationError('Курс должен быть от 1 до 6.')
        return value
