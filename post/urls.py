from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PostListCreateView, PostDetailView

router = DefaultRouter()
router.register('', PostViewSet)

urlpatterns = [
    path('create/', PostListCreateView.as_view()),
    path('detail/<int:id>/', PostDetailView.as_view()),
    path('', include(router.urls)),
]


