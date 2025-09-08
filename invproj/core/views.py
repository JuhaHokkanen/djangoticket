from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView
from .models import Device, Ticket

class DeviceList(LoginRequiredMixin, ListView):
    model = Device
    ordering = ['-created_at']

class DeviceCreate(LoginRequiredMixin, CreateView):
    model = Device
    fields = ['name','serial','location']
    success_url = reverse_lazy('device_list')

class DeviceDelete(LoginRequiredMixin, DeleteView):
    model = Device
    success_url = reverse_lazy('device_list')

class TicketList(LoginRequiredMixin, ListView):
    model = Ticket
    queryset = Ticket.objects.select_related('device').order_by('-created_at')

class TicketCreate(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['device','title','description','status']
    success_url = reverse_lazy('ticket_list')

class TicketDelete(LoginRequiredMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy('ticket_list')
