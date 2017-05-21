# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import userDB

def index(request):
    return render(request, 'LoginAndRegistration/index.html')

def login(request):
    if request.method == "POST":
        #Validate information
        response = userDB.objects.login_check(request.POST)
        #Show errors and redirect to index if information incorrect
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
            return redirect('/')
        else:
            request.session['user'] = {
                "first_name": response[1].first_name,
                "last_name": response[1].last_name,
                "id": response[1].id,
            }
            #Redirect user to the wall once information is validated
        return redirect('/wall')

def register(request):
    if request.method == "POST":
        #Validate information
        response = userDB.objects.user_check(request.POST)
        #Show errors and redirect to index if information incorrect
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
            return redirect('/')
        else:
            request.session['user'] = {
                "first_name": response[1].first_name,
                "last_name": response[1].last_name,
                "id": response[1].id,
            }
            #Redirect user to the wall once information is validated and entered into databases
            return redirect('/wall')

# Create your views here.
