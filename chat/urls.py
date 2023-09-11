from rest_framework.routers import DefaultRouter

from chat.views import UserViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = router.urls
