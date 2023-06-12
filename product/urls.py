from django.urls import path,include
from rest_framework.routers  import DefaultRouter
from .views import ProductViewSet,OrderView

router = DefaultRouter()
router .register('products', ProductViewSet)
router.register('orders', OrderView)

urlpatterns = [
    path('',include(router.urls))
]