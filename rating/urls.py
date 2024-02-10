from django.urls import path
from .views import RatingCreate, RatingRetrieveUpdateDestroy

urlpatterns = [
    path('ratings/', RatingCreate.as_view(), name='rating-create'),
    path('ratings/<int:pk>/', RatingRetrieveUpdateDestroy.as_view(), name='rating-detail'),
]
