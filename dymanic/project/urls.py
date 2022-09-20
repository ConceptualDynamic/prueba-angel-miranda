from rest_framework import routers
from django.urls import path
from .api import ClientViewSet, ProductViewSet, RegisterAPI

router = routers.DefaultRouter()
router.register('api/client', ClientViewSet, 'client')
router.register('api/product', ProductViewSet, 'product')

urlpatterns = router.urls
# urlpatterns = [
    
#     path('api/register/', RegisterAPI.as_view(), name='register'),
# ]