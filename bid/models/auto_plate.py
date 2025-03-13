from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.timezone import now
from .base import Base
from django.db import models
from .user import User


class CustomManager(models.Manager):
    def search(self, q):
        return self.get_queryset().filter(Q(region__icontains=q) | Q(plate_number__icontains=q) | Q(region_int__icontains=q))

class AutoPlate(Base):
    region = models.CharField(max_length=30)
    region_int = models.IntegerField()
    plate_number = models.CharField(max_length=8, unique=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    start_price = models.DecimalField(max_digits=5, decimal_places=2)

    objects = CustomManager()

    def save(self, *args, **kwargs):
        if self.deadline <= now():
            raise ValidationError("Deadline must be in the future.")
        super().save(*args, **kwargs)