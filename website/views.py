from django.shortcuts import render
from django.http import HttpResponse
import pandas

# Create your views here.
def index(request):
    return render(request, 'adm/index1.html', {'overflow_hidden':True})
