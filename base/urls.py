from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDeleteView,
    ModelsListCreateView,
    ModelsRetrieveUpdateDeleteView,
    api_root
)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view(), name='category-detail'),
    path('models/', ModelsListCreateView.as_view(), name='models-list-create'),
    path('models/<int:pk>/', ModelsRetrieveUpdateDeleteView.as_view(), name='models-detail'),
]
