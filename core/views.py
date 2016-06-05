from django.http import HttpResponse
from django.shortcuts import render
from core import models
# Create your views here.

# def index(request):
#
#     return render(request, 'index.html', {})

def get_exp_teacher(request, s_id):
    s = models.Subject.objects.get(pk=int(s_id))
    t = models.Teacher.objects.filter(subject=s)
    v = []
    for x in t:
        v.append(x.ex)
    teachers = models.Teacher.objects.filter(ex__exact=max(v))

    return render(request, 'teacher.html', {'teachers': teachers})

def get_most_young_student(request, t_id):
    t = models.Teacher.objects.get(pk=int(t_id))
    v = models.MarkList.objects.filter(teacher=t)
    s = []
    for x in v:
        s.append(x.student.birth)

    if s:
        date = max(s)
        students = models.Student.objects.filter(birth__exact=date)
    else:
        students = []

    return render(request, 'students.html', {'students': students})

def get_teachers_with_the_same_profile(request, t_id):
    t_id = int(t_id)
    t = models.Teacher.objects.get(pk=t_id)
    t1 = models.Teacher.objects.filter(subject=t.subject)
    teachers = []
    for x in t1:
        if x.id != t_id:
            teachers.append(x)

    return render(request, 'teachers.html', {'teachers': teachers})

def get_teachers(request):
    teachers = models.Teacher.objects.all()

    return render(request, 'teachers.html', {'teachers': teachers})

def get_subjects(request):
    subjects = models.Subject.objects.all()

    return render(request, 'subjects.html', {'subjects': subjects})