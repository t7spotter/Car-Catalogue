from django.urls import path

from catalouge import views



urlpatterns = [
    path('list-create-company', views.ListCreateCompany.as_view())
]

