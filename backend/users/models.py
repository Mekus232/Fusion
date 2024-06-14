from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
ROLE = (
    ('student', 'Student'),
    ('teacher', 'Teacher')
)
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, null= False, blank= False)
    last_name = models.CharField(max_length=50, null= False, blank= False)
    role = models.CharField(max_length=50, choices = ROLE)

    def __str__(self):
        return self.username
    