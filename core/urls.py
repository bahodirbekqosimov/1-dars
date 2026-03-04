from rest_framework.routers import DefaultRouter 
from . import views

router = DefaultRouter()
router.register('brand',views.BrandViewSet)
router.register('car',views.CarViewSet)



urlpatterns = router.urls