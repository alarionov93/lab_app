from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=False, null=False, blank=False, max_length=255, verbose_name='Имя')

    class Meta:
        db_table = 'students'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=False, null=False, blank=False, max_length=255, verbose_name='Имя')

    class Meta:
        db_table = 'teachers'
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=False, null=False, blank=False, max_length=255, verbose_name='Имя')

    class Meta:
        db_table = 'subjects'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class MarkList(models.Model):
    id = models.AutoField(primary_key=True)
    mark = models.CharField(unique=False, null=False, blank=False, max_length=255, verbose_name='Имя')
    subject = models.ForeignKey('Subject', to_field='id', db_column='subject_id',
                                unique=False, blank=False, null=False)

    class Meta:
        db_table = 'subjects'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'