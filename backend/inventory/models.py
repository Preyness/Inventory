from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

def validate_positive(value):
    if value < 0:
        raise ValidationError(f"{value} is not a positive number")

ROOM_CHOICES = [
    ('PR', 'Prep Room'),
    ('MS', 'Main Stockroom'),
    ('2F', '2nd Floor Chem. Lab'),
]

class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=2, choices=ROOM_CHOICES, default='PR')

    def __str__(self):
        return self.name

class Category(models.Model):  # New Category model
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # New field
    date = models.DateField()
    qty = models.IntegerField(validators=[validate_positive])
    unit = models.CharField(max_length=50)
    breakages = models.IntegerField(validators=[validate_positive])
    balance = models.IntegerField(validators=[validate_positive])
    remarks = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_balance(self):
        return self.qty - self.breakages

    def __str__(self):
        return self.name
