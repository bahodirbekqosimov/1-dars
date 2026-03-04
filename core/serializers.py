from rest_framework import serializers
from .models import Car, Brand
from rest_framework.exceptions import ValidationError
from datetime import datetime as dt

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id','name', 'image', 'summary','created_at', ]
        read_only_fields = ['id','created_at']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','car_model','name', 'year', 'price', 'engine', 'brand', 'mileage', 'fuel_type', 'transmission', 'color', 'description', 'image','created_at' ]
        read_only_fields = ['id','created_at',]

    def validate_year(self, year):
        if type(year)!=int:
            return ValidationError('year must be an integer', code=400)
        if year<dt.now().year-50:
            return ValidationError("The car must be under 50 years old.", 400)
        if year>dt.now().year:
            return ValidationError("It can't be next year.", code=400)
        return year
    def validate_price(self, price):
        if price <0:
            return ValidationError('price must not be less than 0',400)
        return price
        
    def validate_mileage(self, mileage):
        if mileage <0:
            return ValidationError('mileage must not be less than 0',400)
        return mileage
        


    