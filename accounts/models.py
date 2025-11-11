from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from schedule.models import Group

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="ФИО")
    role = models.CharField(
        max_length=20,
        choices=[
            ('teacher', 'Преподаватель'),
            ('admin', 'Администратор'),
            ('student', 'Студент'),
        ],
        default='student',
        verbose_name="Роль"
    )
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Группа")

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()