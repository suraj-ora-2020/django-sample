from django.shortcuts import render
from django.http import HttpResponse
from .models import emp
from pprint import pprint
import os
import time

def empv(request):

    res = "List of all employees <br> "
    objects = emp.objects.all()
    for empl in objects:
    	res+= empl.ename+'<br>' 

    return HttpResponse(res)

