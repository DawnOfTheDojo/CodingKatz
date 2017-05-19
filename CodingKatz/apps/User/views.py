# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def user(request):
    #confirm user id is logged in to view that page

    #Retrieve user information from the database to be displayed on the page

    #Display user page
    return render(request, 'User/user.html')

def edit(request):
    #Content from edit form

    #Validate content from form

    #Ensure if email is updated that it is also not already used in database

    #Update database with new content

    #Redirect user to user profile page
    return redirect('/user')

def delete(request):
    #Confirm user wants to delete their account

    #Consider whether to Cascade delete user's information, messages, and comments from the database

    #Potential for 'recover account' for users which will bring back all their data

    #Return former user to landing page
    return redirect('/')

# Create your views here.
