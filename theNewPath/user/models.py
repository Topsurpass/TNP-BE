from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.URLField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=10, choices=[('user', 'User'), ('mentor', 'Mentor'), ('admin', 'Admin')], default='user')
    program_final_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=0.0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True,
    )
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

