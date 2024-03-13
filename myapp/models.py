from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, phone_number=None):
        user = self.create_user(
            email=email,
            password=password,
            phone_number=phone_number,
        )
        user.staff = True
        user.admin = True
        user.save()
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']


class Organization(models.Model):
    users = models.ManyToManyField(User, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization)
    image = models.ImageField(upload_to='events/')
    date = models.DateTimeField()
