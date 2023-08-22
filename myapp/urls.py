
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('cindex/',views.cindex,name='cindex'),
    path('customer/',views.customer,name='customer'),
    path('customersignup/',views.customersignup,name='customersignup'),
    path('login/',views.login,name='login'),
    path('loout/',views.logout,name='logout'),

]
