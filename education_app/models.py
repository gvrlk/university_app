from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Work(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True,
        help_text='Название практической работы',
    )
    description = models.TextField(
        help_text='Описание практической работы',
    )
    students = models.ManyToManyField(
        User,
        through='Assessment',
        through_fields=('work', 'student'),
        related_name='student_works',
    )
    teachers = models.ManyToManyField(
        User,
        through='Assessment',
        through_fields=('work', 'teacher'),
        related_name='teacher_works',
    )

    def __str__(self):
        return f'Работа "{self.name}"'


class Assessment(models.Model):
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name='assessments',
        help_text='Оцениваемая практическая работа студента',
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_assessments',
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='teacher_assessments'
    )
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Количество баллов за работу',
    )
    comment = models.TextField(
        help_text='Комментарий к оценке',
    )

    def __str__(self):
        return f'{self.teacher.username}-{self.student.username}: {self.score} {self.comment}'
