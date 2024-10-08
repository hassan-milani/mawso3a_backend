from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BabViewSet, MawdoeViewSet, PageViewSet

router = DefaultRouter()
router.register(r'babs', BabViewSet)
router.register(r'mawdoes', MawdoeViewSet)
router.register(r'pages', PageViewSet)

urlpatterns = [
 
]

urlpatterns += router.urls