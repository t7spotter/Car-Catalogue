from rest_framework import serializers

from .models import Category, Car, Company


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"