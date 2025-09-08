from django.urls import path
from . import views


urlpatterns = [
path('', views.DeviceList.as_view(), name='device_list'),
path('devices/add/', views.DeviceCreate.as_view(), name='device_add'),
path('devices/<int:pk>/delete/', views.DeviceDelete.as_view(), name='device_delete'),


path('tickets/', views.TicketList.as_view(), name='ticket_list'),
path('tickets/add/', views.TicketCreate.as_view(), name='ticket_add'),
path('tickets/<int:pk>/delete/', views.TicketDelete.as_view(), name='ticket_delete'),
]