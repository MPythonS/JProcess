from django.urls import path
from orders import views
from orders.views import create_order, hello_view, success_page, order_list, home
from users.views import user_login_view, user_logout_view

urlpatterns = [
    path('hello/', hello_view),
    path('order/', create_order, name='order_form'), #  create_order paimtas iš order\views.py
    path('success/', success_page, name='success_page'),  # is create_order pakeista i hello_view
    path('order_list/', order_list, name='order_list'), #  create_order paimtas iš order\views.py
    path('order/<int:pk>/edit/', views.order_edit, name='order_edit'),
    path('order/<int:pk>/delete/', views.order_delete, name='order_delete'),
    path('', home, name='pradinis'),
    path('login/', user_login_view, name='login'),
    path('send_email/<int:pk>/', views.send_email, name='send_email'),
    path('logout/', user_logout_view, name='logout')

]
