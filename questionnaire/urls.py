from django.urls import path
from questionnaire import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event_overview/<int:event_id>', views.event_overview, name='event_overview'),
    path('event_detail/<int:event_id>/<int:classification>/<int:main_id>', views.event_detail, name='event_detail'),
    path('create_result', views.create_result, name='create_result'),
]