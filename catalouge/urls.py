from django.urls import path

from catalouge import views



urlpatterns = [
    path('list-create-company/', views.ListCreateCompany.as_view()),
    path('list-create-company/<int:pk>', views.RetrieveCompany.as_view()),
    
    path('list-create-category/', views.ListCreateCategory.as_view()),
    path('list-create-category/<int:pk>', views.RetrieveCategory.as_view()),
    
    path('list-create-car/', views.ListCreateCar.as_view()),
    path('list-create-car/<int:pk>', views.RetrieveCar.as_view()),
    
    
]

