from django import forms
from .models import Lesson, Group, Classroom, Subject

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['group', 'subject', 'classroom', 'date', 'start_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        lesson = super().save(commit=False)
        start = self.cleaned_data['start_time']
        lesson.end_time = self.add_90_minutes(start)
        if commit:
            lesson.save()
        return lesson

    def add_90_minutes(self, time_obj):
        from datetime import timedelta, datetime
        dt = datetime.combine(datetime.today(), time_obj)
        dt += timedelta(minutes=90)
        return dt.time()

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'capacity']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'teacher']