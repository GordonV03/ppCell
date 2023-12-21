from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.forms import fields
from .models import UploadImage
from django import forms
# Create your views here.
from django.shortcuts import redirect, render

from .models import UploadImage


def index(request):
    return render(request, 'main/index.html')



