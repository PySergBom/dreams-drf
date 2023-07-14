from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from my_dreams.models import Dream
from my_dreams.serializers.dream_serializer import DreamSerializer


class DreamViewSet(ModelViewSet):
    queryset = Dream.objects.all()
    serializer_class = DreamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

