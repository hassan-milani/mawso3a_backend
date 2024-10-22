from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import Bab, Mawdoe, Page
from .serializers import BabSerializer, MawdoeSerializer, PageSerializer
from .permissions import HasRolePermission

#Query parameter schema for bab_id
bab_id_param = openapi.Parameter(
    'bab_id',
    openapi.IN_QUERY,
    description="Filter by Bab ID",
    type=openapi.TYPE_STRING
)
#Query parameter schema for mawdoe_id
mawdoe_id_param = openapi.Parameter(
    'mawdoe_id',
    openapi.IN_QUERY,
    description="Filter by Mawdoe ID",
    type=openapi.TYPE_STRING
)

class BabViewSet(viewsets.ModelViewSet):
    queryset = Bab.objects.all()
    serializer_class = BabSerializer
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasRolePermission]
    required_role = ['admin', 'editor']


class MawdoeViewSet(viewsets.ModelViewSet):
    queryset = Mawdoe.objects.all()
    serializer_class = MawdoeSerializer
    permission_classes = [IsAuthenticated, HasRolePermission]
    required_role = ['admin', 'editor']
    

    def get_queryset(self):
        """
        Optionally filter mawdoes by a given bab_id (passed as a query parameter).
        """
        queryset = Mawdoe.objects.all()
        bab_id = self.request.query_params.get('bab_id')  # Get bab_id from query parameters
        
        # Debug to ensure `bab_id` is being captured
        print(f"bab_id: {bab_id}")

        if bab_id:
            queryset = queryset.filter(bab__id=bab_id)  # Filter the queryset by bab__id (foreign key)
        return queryset
    
    @swagger_auto_schema(manual_parameters=[bab_id_param])
    def list(self, request, *args, **kwargs):
        """
        Optionally filter mawdoes by bab_id query parameter.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasRolePermission]
    required_role = ['admin', 'editor']
    
    def get_queryset(self):
        """
        Optionally filter mawdoes by a given mawdoe_id (passed as a query parameter).
        """
        queryset = Page.objects.all()
        mawdoe_id = self.request.query_params.get('mawdoe_id')  # Get mawdoe_id from query parameters
        
        # Debug to ensure `mawdoe_id` is being captured
        print(f"mawdoe_id: {mawdoe_id}")

        if mawdoe_id:
            queryset = queryset.filter(mawdoe__id=mawdoe_id)  # Filter the queryset by mawdoe__id (foreign key)
        return queryset
    
    @swagger_auto_schema(manual_parameters=[mawdoe_id_param])
    def list(self, request, *args, **kwargs):
        """
        Optionally filter mawdoes by mawdoe_id query parameter.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

