from django.urls import path
from . import views

urlpatterns = [
    path('brand/', views.BrandListCreateAPIView.as_view()),
    path('brand/<int:pk>/', views.BrandDetailAPIView.as_view()),
    path('car/',views.CarListCreateAPIView.as_view()),
    path('car/<int:pk>/', views.CarDetailAPIView.as_view())
]
