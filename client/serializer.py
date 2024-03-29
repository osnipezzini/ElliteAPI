# _*_ coding: UTF-8 _*_
'''
Created on 05/06/2019
@author: osnip
'''
from rest_framework import serializers
from rest_framework.fields import URLField

from key.serializer import KeySerializer
from product.serializer import ProductSerializer
from .models import Company, Client


class CompanySerializer(serializers.ModelSerializer):
    key = KeySerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = Company
        fields = ('__all__')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')
