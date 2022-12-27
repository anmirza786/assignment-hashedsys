
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework.permissions import AllowAny
from core.serializers import CategorySerializer
from core.models import Category


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
    A simple ViewSet for viewing and editing Category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def create(self, request, pk=None):
        if request.method == 'POST':
            serializer = CategorySerializer(data=request.data)

            if serializer.is_valid():
                id = serializer.validated_data['category_name']
                print(id)
                try:
                    Category = Category.objects.get_or_create(
                        category_name=id)
                except:
                    return Response({'message': 'Category not found'})

        return super().create(request)

    def delete(self, request, pk=None):
        if request.method == 'DELETE':
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                id = serializer.validated_data['id']
                try:
                    category = Category.objects.get(
                        id=id)
                    category.save()
                    return Response({'message': 'Category Deleted'})
                except:
                    return Response({'message': 'Category not found'})

        return super().delete(request)
