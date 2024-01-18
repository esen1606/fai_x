from django.urls import path
from .views import add_like, remove_like

urlpatterns = [
    path('add/<int:post_id>/', add_like, name='add_like'),
    path('delete/<int:post_id>/', remove_like, name='remove_like'),
]
