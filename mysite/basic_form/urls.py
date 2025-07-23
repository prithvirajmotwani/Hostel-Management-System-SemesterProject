from django.contrib import admin
from django.urls import path

from basic_form import views

urlpatterns = [
    path ('', views.home, name="home"),

    path('home/<notification_id>', views.home, name='home1'),
    # path('<notification_id>', views.home, name='home'),
    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name='logoutUser'),


    path('profile', views.profile, name='profile'),


    
    path('invoices', views.invoices, name='invoices'),
    path('roomChange', views.roomChange, name='room_change'),
    path('outpass', views.outpass, name='outpass'),
    path('report-a-problem', views.rAP, name='rAP'),
    path('create-account', views.createACC, name='rAP'),
    path('allStudents', views.allStudents, name='std'),
    path('allManagers', views.allManagers, name='mngrs'),
    path('attendance', views.attendance, name='atndc'),
    path('invoices/submit', views.invoicesSubmit, name='invcSubmit'),
    path('downloadInvoice', views.invoiceCreate, name='invcSubmit'),


]
