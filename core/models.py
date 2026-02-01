
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
	def create_user(self, username, password=None, role="student", **extra_fields):
		if not username:
			raise ValueError("The Username must be set")
		user = self.model(username=username, role=role, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		return self.create_user(username, password, role="teacher", **extra_fields)

class User(AbstractBaseUser):
	ROLE_CHOICES = [
		("teacher", "Teacher"),
		("student", "Student"),
	]
	username = models.CharField(max_length=150, unique=True)
	role = models.CharField(max_length=10, choices=ROLE_CHOICES)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['role']

	def __str__(self):
		return f"{self.username} ({self.get_role_display()})"

