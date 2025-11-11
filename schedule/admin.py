from django.contrib import admin
from .models import Group, Classroom, Subject, Lesson

admin.site.register(Group)
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(Lesson)