from django.urls import path , include

from main import views

app_name = 'api'

urlpatterns = [
    path('', views.companies_view),
    path('add_Employee/<int:company_id>/', views.add_employee, name='add_Employee'),
    path('select2/', include('django_select2.urls')),
]
