from rest_framework import serializers
from .helpers import more_adding_warehouse_product
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["excel_product"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["order"] = instance.id
        return representation


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

