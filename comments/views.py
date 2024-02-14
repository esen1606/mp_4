from django.shortcuts import render
from .models import Comment
from rest_framework import generics, permissions
from account.permissions import IsAuthor
from .serializers import CommentSerializer
import logging
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
logger = logging.getLogger(__name__)


@method_decorator(cache_page(60*10), name='dispatch')
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permissions = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAuthor(), permissions.IsAdminUser()]
        return [permissions.AllowAny()]