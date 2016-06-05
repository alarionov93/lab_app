from core import views
from django.conf.urls import url

urlpatterns = [
    # url(r'^', views.index, name='index_page'),
    url(r'^subjects/all/', views.get_subjects, name='all_subjects'),
    url(r'^subj/(?P<s_id>[0-9]+)/teachers', views.get_exp_teacher, name='most_exp_teacher'),
    url(r'^teacher/(?P<t_id>[0-9]+)/youngest/', views.get_most_young_student, name='most_young_student'),
    url(r'^teachers/all/', views.get_teachers, name='all_teachers'),
    url(r'^teachers/(?P<t_id>[0-9]+)/similar/', views.get_teachers_with_the_same_profile,
        name='similar_teachers'),
]