from django.urls import path, include
from . import views

urlpatterns = [
    path('buy/', views.CreateCheckoutSession.as_view(), name='create-checkout-session'),
]
