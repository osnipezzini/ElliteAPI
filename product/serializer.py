# _*_ coding: UTF-8 _*_

'''
Created on 05/06/2019
@author: osnip
'''
from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')
