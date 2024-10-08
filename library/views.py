from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Bab, Mawdoe, Page
from .serializers import BabSerializer, MawdoeSerializer, PageSerializer
from .permissions import HasRolePermission


class BabViewSet(viewsets.ModelViewSet):
    queryset = Bab.objects.all()
    serializer_class = BabSerializer
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasRolePermission]
    required_role = ['admin', 'editor']


class MawdoeViewSet(viewsets.ModelViewSet):
    queryset = Mawdoe.objects.all()
    serializer_class = MawdoeSerializer
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasRolePermission]
    required_role = ['admin', 'editor']

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasRolePermission]
    required_role = ['admin', 'editor']

