from rest_framework import generics

from .models import Car, Company, Category
from .serializers import CarSerializer, CompanySerializer, CategorySerializer


class ListCreateCompany(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    
class RetrieveCompany(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    

class ListCreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class RetrieveCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ListCreateCar(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    

class RetrieveCar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer