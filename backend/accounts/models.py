from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os

class LabTechUser(AbstractUser):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    is_labtech = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    pass

#automatic mag create og superuser didto ra kuhaon sa .env  
@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'accounts':
        User = LabTechUser
        username = os.getenv('DJANGO_ADMIN_USERNAME')
        email = os.getenv('DJANGO_ADMIN_EMAIL')
        password = os.getenv('DJANGO_ADMIN_PASSWORD')

        if not User.objects.filter(username=username).exists():
            # Create the superuser with is_active set to False
            superuser = User.objects.create_superuser(
                username=username, email=email, password=password)

            # Activate the superuser
            superuser.is_active = True
            print('Created admin account')
            superuser.save()
