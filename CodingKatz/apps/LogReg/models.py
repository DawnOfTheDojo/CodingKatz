# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

EMAILREG = re.compile(r'[a-zA-Z0-9.-_+]+@[a-zA-Z0-9.-_]+\.[a-zA-Z]*$')

class userDBManager(models.Manager):
    def check_create(self, data):
        errors = []
        if len(data['first_name']) < 2:
            errors.append(['first_name', "First name must be at least two characters in length."])
        if len(data['last_name']) < 2:
            errors.append(['last_name', "Last name must be at least two characters in length."])
        if not re.match(EMAILREG, data['email']):
            errors.append(['email', "Email must be a valid email address."])
        if errors:
            return [False, errors]
        else:
            newUser = userDB(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'])
            newUser.save()
            return [True, newUser]

    def check_login(self, data):
        errors = []
        if not re.match(EMAILREG, data['email']):
            errors.append(['email', "Email must be a valid email address."])
        if len(data['password']) < 8:
            errors.append(['password', 'Password must be at least 8 characters.'])
        if errors:
            return [False, errors]
        else:
            check_user = userDB.objects.filter(email=data['email'])
            if not check_user:
                errors.append(['login', "Email or password not correct.  Please try again."])
            if not bcrypt.checkpw(data['password'].encode(), check_user[0].password.encode()):
                errors.append(['login', "Email or password not correct.  Please try again."])
            if errors:
                return [False, errors]
            else:
                user = check_user[0]
                print user
                return [True, user]
# Create your models here.
class userDB(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    created_at=DateTimeField(auto_now_add=True)
    updated_at=DateTimeField(auto_add=True)
    def __str__(self):
        return 'ID: %s | Name: %s %s | Email: %s' % (self.id, self.first_name, self.last_name, self.email)
    objects = userDBManager()
