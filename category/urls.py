from django.urls import path, include
from .views import CategoryDetailView, CategoryCreteListView


urlpatterns = [
    path('create/', CategoryCreteListView.as_view()),
    path('detail/<int:id>/', CategoryDetailView.as_view()),
]
