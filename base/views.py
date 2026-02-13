from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from .models import Category, Models
from .serializers import CategorySerializer, ModelsSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ModelsListCreateView(generics.ListCreateAPIView):
    queryset = Models.objects.all()
    serializer_class = ModelsSerializer

class ModelsRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Models.objects.all()
    serializer_class = ModelsSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'categories': reverse('category-list-create', request=request, format=format),
        'models': reverse('models-list-create', request=request, format=format)
    })
