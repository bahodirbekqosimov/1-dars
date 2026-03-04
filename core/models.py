from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='brands/')
    summary = models.TextField(max_length=1000, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Car(models.Model):


    car_model = models.CharField(max_length=150)
    name = models.CharField(max_length=255, null=True, blank=True)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    engine = models.CharField(max_length=255)

    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, related_name='cars')
    mileage = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=20)
    transmission = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cars/',)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.car_model} ({self.year})"