from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RoleViewSet, UserProfileViewSet, LoginView

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'user-profiles', UserProfileViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += router.urls