from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    template = loader.get_template('homepage/index.html')
    context = {'name':'Trong'}
    return HttpResponse(template.render(context,request))