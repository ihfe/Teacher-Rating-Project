from django.urls import path
from rating import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event_admin', views.event_admin, name='event_admin'),
    path('event_admin/create_event', views.create_event, name='create_event'),
    path('event_admin/delete_event', views.delete_event, name='delete_event'),
    path('event_admin/event_detail', views.event_detail, name='event_detail'),
    path('item_admin', views.item_admin, name='item_admin'),
    path('item_admin/create_item', views.create_item, name='create_item'),
    path('item_admin/delete_item', views.delete_item, name='delete_item'),
    path('event_admin/event_detail/detail_class', views.detail_class, name='detail_class'),
    path('event_admin/event_detail/detail_answer', views.detail_answer, name='detail_answer'),
    path('event_admin/event_detail/detail_aver', views.detail_aver, name='detail_aver'),
]