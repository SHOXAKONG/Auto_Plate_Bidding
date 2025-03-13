from django.core.exceptions import ValidationError
from django.db import models
from .auto_plate import AutoPlate
from .base import Base
from .user import User


class Bid(Base):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, models.CASCADE)
    plate_number = models.ForeignKey(AutoPlate, on_delete=models.CASCADE)

    def clean(self):
        if self.amount < 0:
            raise ValidationError("Amount Should Be Positive")
        return self.amount