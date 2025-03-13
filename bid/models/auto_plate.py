from django.core.exceptions import ValidationError
from django.utils.timezone import now
from .base import Base
from django.db import models
from .user import User

class CustomManage(models.Manager):
    pass

class AutoPlate(Base):
    region = models.CharField(max_length=30)
    region_int = models.IntegerField()
    plate_number = models.CharField(max_length=8, unique=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    start_price = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.deadline <= now():
            raise ValidationError("Deadline must be in the future.")
        super().save(*args, **kwargs)