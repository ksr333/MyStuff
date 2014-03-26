from django.db import models
from django.contrib.auth.models import AbstractUser


class Session(models.Model):
    ##id
    last_accessed = models.DateTimeField(auto_now=True, auto_now_add=True)
    ip_address = models.IntegerField(blank=True, null=True)


class User(AbstractUser):
    ##The following attributes are inherited from Abstract User:
    ## id
    ## password
    ## last_login
    ## is_superuser
    ## username
    ## first_name
    ## last_name
    ## email
    ## is_staff
    ## is_active
    ## date_joined
    is_customer = models.BooleanField(default=False)
    security_answer = models.TextField(blank=True, null=True)


class Address(models.Model):
    ##id
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    street = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zipcode = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)


class UserPhone(models.Model):
    ##id
    user = models.ForeignKey(User)
    is_active = models.BooleanField(default=True)
    phone_type = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)


class SecurityQuestion(models.Model):
    ##id
    user = models.ForeignKey(User)
    is_active = models.BooleanField(default=True)
    security_question = models.TextField(blank=True, null=True)


class Member(models.Model):
    ##id
    user = models.OneToOneField(User, primary_key=True)
    membership_date = models.DateField()
    want_newsletter = models.BooleanField(default=True)


class NewsletterInterestAreas(models.Model):
    ##id
    is_active = models.BooleanField()
    member = models.ForeignKey(Member)
    areas_of_interest = models.TextField(blank=True, null=True)


class Employee(models.Model):
    ##id
    user = models.OneToOneField(User, primary_key=True)
    hire_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    salary = models.DecimalField(max_digits=50, decimal_places=2)
    position = models.TextField(blank=True, null=True)


class Commission(models.Model):
    ##id
    employee_information = models.ForeignKey(Employee)
    amount = models.DecimalField(max_digits=50, decimal_places=2)
    date = models.DateField()


