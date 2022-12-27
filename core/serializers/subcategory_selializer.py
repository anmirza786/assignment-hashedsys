from core.models import SubCategory
from rest_framework import serializers
from .category_selializer import CategorySerializer


class SubCategorySerializer(serializers.ModelSerializer):
    # category_type = CategorySerializer(read_only=True)
    category_type = serializers.IntegerField(
        source='category_type.id', read_only=False)

    class Meta:
        model = SubCategory
        fields = "__all__"
