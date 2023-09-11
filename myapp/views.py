from django.shortcuts import render
from django.http import HttpResponse
from .models import Emp
from pprint import pprint
import os

def empv(request):

    res = "List of all employees <br> "
    objects = Emp.objects.all()
    for emp in objects:
    	res+= emp.ename+'<br>' 

    return HttpResponse(res)

