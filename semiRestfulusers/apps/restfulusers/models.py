from __future__ import unicode_literals

from django.db import models
import re, datetime, time
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['full_name']) < 4:
            errors["name"] = "User full name should be more than 4 characters"
        if len(postData['email']) < 1:
            errors['email'] = "Invalid Email Address!"
        elif not EMAIL_REGEX.match(postData['email']):           
            errors['invalid_email'] = "Invalid Email Address!"
        
        return errors
            


class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {}".format(self.full_name, self.email)