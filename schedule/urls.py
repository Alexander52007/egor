from django.urls import path
from . import views

urlpatterns = [
    path('my-schedule/', views.my_schedule, name='my_schedule'),
    path('add-lesson/', views.add_lesson, name='add_lesson'),
    path('manage-groups/', views.manage_groups, name='manage_groups'),
    path('manage-classrooms/', views.manage_classrooms, name='manage_classrooms'),
    path('manage-subjects/', views.manage_subjects, name='manage_subjects'),
    path('add-group/', views.add_group_as_student, name='add_group_as_student'),
]