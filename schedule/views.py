from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Lesson, Group, Classroom, Subject
from .forms import LessonForm, GroupForm, ClassroomForm, SubjectForm


@login_required
def my_schedule(request):
    user = request.user
    lessons = Lesson.objects.none()

    if user.profile.role == 'student':
        if user.profile.group:
            lessons = Lesson.objects.filter(group=user.profile.group).order_by('date', 'start_time')
    else:
        # Преподаватель или админ → показываем его занятия
        lessons = Lesson.objects.filter(subject__teacher=user).order_by('date', 'start_time')

    return render(request, 'schedule/my_schedule.html', {'lessons': lessons})


@login_required
def add_lesson(request):
    if request.user.profile.role != 'teacher':
        messages.error(request, "Только преподаватели могут добавлять занятия.")
        return redirect('my_schedule')

    if request.method == 'POST':
        form = LessonForm(request.POST, user=request.user)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, f"Занятие добавлено: {lesson}")
            return redirect('my_schedule')
        else:
            messages.error(request, "Форма содержит ошибки.")
    else:
        form = LessonForm(user=request.user)

    return render(request, 'schedule/add_lesson.html', {'form': form})


@login_required
def manage_groups(request):
    if request.user.profile.role not in ['teacher', 'admin']:
        return redirect('profile')

    groups = Group.objects.all()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Группа добавлена.')
            return redirect('manage_groups')
    else:
        form = GroupForm()
    return render(request, 'schedule/manage_groups.html', {'form': form, 'groups': groups})


@login_required
def manage_classrooms(request):
    if request.user.profile.role not in ['teacher', 'admin']:
        return redirect('profile')

    classrooms = Classroom.objects.all()
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аудитория добавлена.')
            return redirect('manage_classrooms')
    else:
        form = ClassroomForm()
    return render(request, 'schedule/manage_classrooms.html', {'form': form, 'classrooms': classrooms})


@login_required
def manage_subjects(request):
    if request.user.profile.role not in ['teacher', 'admin']:
        return redirect('profile')

    subjects = Subject.objects.all()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Предмет добавлен.')
            return redirect('manage_subjects')
    else:
        form = SubjectForm()
    return render(request, 'schedule/manage_subjects.html', {'form': form, 'subjects': subjects})


def add_group_as_student(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if Group.objects.filter(name=name).exists():
                messages.error(request, 'Группа с таким названием уже существует.')
            else:
                form.save()
                messages.success(request, f'Группа "{name}" добавлена.')
                return redirect('add_group_as_student')
    else:
        form = GroupForm()
    return render(request, 'schedule/add_group_student.html', {'form': form})