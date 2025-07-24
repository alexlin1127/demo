from django.contrib import admin
from django.urls import path, include

# third-party
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

# apps
from tutorial.todos.views import TodoViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'todos', TodoViewSet, basename='todo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
