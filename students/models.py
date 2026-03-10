from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, EmailValidator
from django.db import models


class Student(models.Model):
    """Студент. id — автоинкремент (по умолчанию в Django)."""
    name = models.CharField(
        'Имя',
        max_length=200,
        validators=[MinLengthValidator(2, message='Имя должно быть не короче 2 символов')],
    )
    age = models.PositiveSmallIntegerField(
        'Возраст',
        validators=[
            MinValueValidator(16, message='Возраст должен быть от 16 до 60'),
            MaxValueValidator(60, message='Возраст должен быть от 16 до 60'),
        ],
    )
    email = models.EmailField('Email', validators=[EmailValidator(message='Введите корректный email')])
    course = models.PositiveSmallIntegerField(
        'Курс',
        validators=[
            MinValueValidator(1, message='Курс должен быть от 1 до 6'),
            MaxValueValidator(6, message='Курс должен быть от 1 до 6'),
        ],
    )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} (курс {self.course})'
