from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Device(models.Model):
    name = models.CharField(max_length=120)
    serial = models.CharField(max_length=120, unique=True)
    location = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} ({self.serial})"


class Ticket(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='tickets')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[('open','Open'),('done','Done')], default='open')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"#{self.id} {self.title}"