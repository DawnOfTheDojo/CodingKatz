# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'LoginAndRegistration/index.html')

def login(request):
    #Get email and password from landing page form
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']

    #Validate information

    #Once message is flashed, redirect user with login information still in form to be corrected.
    # if messages.error:
    #     return redirect('/')

    #Redirect user to the wall once information is validated
    return redirect('/wall')

def register(request):
    #Get information for user from registration form
    user = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'confirm_password': request.POST['confirm_password'],
    }

    #Validate information

    #Enter information into database

    #Capture user_id in session

    #Redirect user to the wall once information is validated and entered into databases
    return redirect('/wall')

# Create your views here.
