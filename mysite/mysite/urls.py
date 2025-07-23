from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('basic_form.urls')),
    path('home/<notification_id>', include('basic_form.urls')),
    # path('<notification_id>', include('basic_form.urls')),
    path('login', include('basic_form.urls')),
    path('logout', include('basic_form.urls')),
    path('save', include('basic_form.urls')),


    path('profile', include('basic_form.urls')),




    
    path('invoices', include('basic_form.urls')),
    path('roomChange', include('basic_form.urls')),
    path('outpass', include('basic_form.urls')),
    path('report-a-problem', include('basic_form.urls')),
    path('create-account', include('basic_form.urls')),
    path('allStudents', include('basic_form.urls')),
    path('allManagers', include('basic_form.urls')),
    path('attendance', include('basic_form.urls')),
    path('invoices/submit', include('basic_form.urls')),
    path('downloadInvoice', include('basic_form.urls')),

]
