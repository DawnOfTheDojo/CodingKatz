# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def wall(request):
    #Stuff!

    return render(request, 'Wall/wall.html')

def message(request):
    #Content from message

    #Validate content

    #Put message in database

    #Return message to page for display
    return redirect('/wall')

def comment(request):
    #Content from comment

    #Validate content

    #Put comment in database

    #Return comment to page for display
    return redirect('/wall')

def deleteMessage(request):
    #Figure out how to do confirmation for deletion (possibly pop up alert)

    #Delete message from database

    #Return user to page through redirect
    return redirect('/wall')

def deleteComment(request):
    #Figure out how to do confirmation for deletion (possibly pop up alert)

    #Delete comment from database

    #Return user to page through redirect
    return redirect('/wall')




# Create your views here.
