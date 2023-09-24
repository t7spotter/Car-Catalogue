from rest_framework import serializers

from .models import Category, Car, Company


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
        
class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = "__all__"
        

class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fiels = "__all__"