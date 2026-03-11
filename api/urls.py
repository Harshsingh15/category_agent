from django.urls import path
from .views import categorize_transaction, health

urlpatterns = [
    path('categorize/', categorize_transaction),
    path('health/', health),
]