from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.add_course, name='add_course'),
    path('lecturers', views.add_lecturer, name='add_lecturer'),
    path('all_courses', views.see_all_courses, name='all_courses'),
    path('search_courses', views.search_course, name='search_courses'),
    path('to_be_continued', views.to_be_continued, name='to_be_continued'),

]
