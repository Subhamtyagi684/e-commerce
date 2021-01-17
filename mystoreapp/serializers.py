from rest_framework import serializers
from .models import Product
from datetime import datetime
from rest_framework.parsers import MultiPartParser, FormParser , FileUploadParser, JSONParser

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id','prod_name','prod_type','prod_desc','prod_image','prod_price')
