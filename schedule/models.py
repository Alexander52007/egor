from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название группы")

    def __str__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название аудитории")
    capacity = models.PositiveIntegerField(verbose_name="Вместимость")

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название предмета")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Преподаватель")

    def __str__(self):
        return f"{self.name} ({self.teacher.username})"

class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, verbose_name="Аудитория")
    date = models.DateField(verbose_name="Дата")
    start_time = models.TimeField(verbose_name="Начало")
    end_time = models.TimeField(verbose_name="Окончание")

    def __str__(self):
        return f"{self.group} — {self.subject} ({self.date})"

    class Meta:
        ordering = ['date', 'start_time']