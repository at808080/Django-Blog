from django.shortcuts import render
import sys
from sys.path.append('/utils/') import stock

# Create your views here.

def home(request):
    context = {
        'title': 'Home Page',
    }
    return render(request, 'stocks/home.html', context)

def stocks(request):
    

    context = {
        'title': 'About Page',
    }
    return render(request, 'stocks/stock.html', context)
