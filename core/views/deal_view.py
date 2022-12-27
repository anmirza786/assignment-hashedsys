
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework.permissions import AllowAny
from core.serializers import DealSerializer
from core.models import Deal, Category, SubCategory, Business, City


class DealViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
    A simple ViewSet for viewing and editing Category.
    """
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = [AllowAny]

    def create(self, request, pk=None):
        if request.method == 'POST':
            serializer = DealSerializer(data=request.data)
            if serializer.is_valid():
                # id = serializer.validated_data['category_type']
                print(serializer.validated_data)
                # subcategory_name = serializer.validated_data['subcategory_name']
                # subcategory_status = serializer.validated_data['subcategory_status']
                try:
                    # category = Category.objects.get(id=id['id'])
                    print("haha")
                    # subCategory = SubCategory.objects.create(
                    #     category_type=category, subcategory_name=subcategory_name, subcategory_status=subcategory_status)
                    # subCategory.save()
                    # return Response(serializer.data)
                except:
                    return Response({'message': 'Sub Category not found'})

        return super().create(request)

    def delete(self, request, pk=None):
        if request.method == 'DELETE':
            serializer = DealSerializer(data=request.data)
            if serializer.is_valid():
                id = serializer.validated_data['id']
                try:
                    requsistion = Deal.objects.get(
                        id=id)
                    requsistion.save()
                except:
                    return Response({'message': 'Sub Category not found'})

        return super().delete(request)
