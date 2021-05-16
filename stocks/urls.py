from django.urls import path
from . import views
from .views import home, stocks

urlpatterns = [
    path('', home, name='stocks-home'),
    path('stocks/', stocks, name='stocks_stocks')
]
