from rest_framework import generics

from .models import Car, Company, Category
from .serializers import CarSerializer, CompanySerializer, CategorySerializer


class ListCreateCompany(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer