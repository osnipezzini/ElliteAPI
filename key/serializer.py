# _*_ coding: UTF-8 _*_

'''
Created on 05/06/2019
@author: osnip
'''
from rest_framework import serializers

from key.models import Key


class KeySerializer(serializers.ModelSerializer):
    key = serializers.CharField()
    valid_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Key
        fields = ('key', 'valid_date')
