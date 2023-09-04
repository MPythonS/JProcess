from django.urls import path

from orders.views import create_order
from . import views

urlpatterns = [
    path('login/', views.user_login_view, name='login'),
    path('order/', create_order, name='order_form'),


]