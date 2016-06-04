from django.db import models
from django.utils import timezone
# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=False, null=False, blank=False, max_length=255, verbose_name='Имя')
    birth = models.DateField(unique=False, null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'students'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=False, null=False, blank=False, max_length=255, verbose_name='Имя')
    ex = models.IntegerField(unique=False, null=False, blank=False, verbose_name='Опыт')
    department = models.ForeignKey('Department', to_field='id', db_column='department_id',
                                   unique=False, blank=False, null=False, default=1)
    subject = models.ForeignKey('Subject', to_field='id', db_column='subject_id', unique=False, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teachers'
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=False, null=False, blank=False, max_length=255, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'departments'
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=False, null=False, blank=False, max_length=255, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subjects'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class ControlType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=False, null=False, blank=False, max_length=255, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'c_types'
        verbose_name = 'Тип контроля'
        verbose_name_plural = 'Типы контроля'

class MarkList(models.Model):
    id = models.AutoField(primary_key=True)
    mark = models.CharField(unique=False, null=False, blank=False, max_length=255, verbose_name='Оценка')
    teacher = models.ForeignKey('Teacher', to_field='id', db_column='teacher_id',
                                unique=False, blank=False, null=False)
    student = models.ForeignKey('Student', to_field='id', db_column='student_id',
                                unique=False, blank=False, null=False)
    date = models.DateField(default=timezone.now)
    c_type = models.ForeignKey('ControlType', to_field='id', db_column='c_type_id',
                                unique=False, blank=False, null=False, default=1)

    @property
    def subject(self):
        return self.teacher.subject

    def __str__(self):
        return '%s: %s, %s, %s' % (self.c_type, self.subject, self.date, self.mark)

    class Meta:
        db_table = 'mark_lists'
        verbose_name = 'Ведомость'
        verbose_name_plural = 'Ведомости'