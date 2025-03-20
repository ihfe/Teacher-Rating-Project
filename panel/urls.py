from django.urls import path
from panel import views

urlpatterns = [
    path('', views.index, name='index'),
    path('class_admin', views.class_admin, name='class_admin'),
    path('class_admin/create_class', views.create_class, name='create_class'),
    path('class_admin/delete_class', views.delete_class, name='delete_class'),
    path('lesson_admin', views.lesson_admin, name='lesson_admin'),
    path('lesson_admin/create_lesson', views.create_lesson, name='create_lesson'),
    path('lesson_admin/delete_lesson', views.delete_lesson, name='delete_lesson'),
    path('teacher_admin', views.teacher_admin, name='teacher_admin'),
    path('teacher_admin/create_teacher', views.create_teacher, name='create_teacher'),
    path('teacher_admin/delete_teacher', views.delete_teacher, name='delete_teacher'),
]