# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from ..LogReg.models import userDB
from ..Wall.models import Message, Comment

def profile(request):
    #Confirm user id is logged in to view that page
    if "user" in request.session:
    #User information in session and can be displayed on the page through the template
        context = {
            'user': userDB.objects.get(id=request.session['user']['id']),
        }
    #Display user page
        return render(request, 'User/profile.html', context)
    return redirect('LogReg:index')

#validates information and updates user accordingly
def edit(request):
    #Content from edit form
    if request.method == 'POST':
    #Validate content from form
        response = userDB.objects.check_info_edit(request.POST, request.session['user']['id'])
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
        #Update session user
        request.session['user'] = {
            "first_name": response[1].first_name,
            "last_name": response[1].last_name,
            "id": response[1].id,
        }
    #Redirect user to user profile page
    return redirect('User:profile')

def delete(request):
    #Confirm user wants to delete their account

    #Consider whether to Cascade delete user's information, messages, and comments from the database

    #Potential for 'recover account' for users which will bring back all their data

    #Return former user to landing page
    return redirect('LogReg:index')

# Create your views here.
