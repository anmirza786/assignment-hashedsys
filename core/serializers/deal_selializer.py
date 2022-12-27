from core.models import Deal
from rest_framework import serializers
from .category_selializer import CategorySerializer


class DealSerializer(serializers.ModelSerializer):
    # category_type = CategorySerializer(read_only=True)
    # location = serializers.IntegerField(
    #     source='location.id', read_only=False)
    # cat = serializers.IntegerField(
    #     source='cat.id', read_only=False)
    # business = serializers.IntegerField(
    #     source='business.id', read_only=False)
    # sub_cat = serializers.IntegerField(
    #     source='sub_cat.id', read_only=False)

    class Meta:
        model = Deal
        fields = "__all__"
