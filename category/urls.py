from django.urls import path,include
from .views import CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryViewSet),

urlpatterns = [
    path('', include(router.urls)),
    # path('c/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    # path('categories/', CategoryAPIView.as_view()),
    # path('categories/<slug:slug>/', CategoryAPIView.as_view()),
]