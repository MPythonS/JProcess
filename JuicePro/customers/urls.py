from django.urls import path

from customers import views
from customers.views import customer_list

urlpatterns = [
    path('customer_list/', customer_list, name='customer_list'),
    path('customers/delete/<int:pk>/', views.customer_delete, name='customer_delete'),
]
