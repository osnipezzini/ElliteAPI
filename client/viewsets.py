# _*_ coding: UTF-8 _*_

'''
Created on 05/06/2019
@author: osnip
'''
import datetime

from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from client.models import Company
from client.serializer import CompanySerializer
from key.models import Key
from product.models import Product


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CompanySerializer

    def retrieve(self, request, pk):
        queryset = Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def create(self, request):
        cpf = request.data["cnpj"]
        senha = ''
        if request.data['senha'] != '':
            senha = make_password(request.data['senha'])
        print(senha)
        server_ip = request.data['server_ip']
        name = request.data['name']
        company = Company.objects.create(cnpj=cpf, name=name, server_ip=server_ip, password=senha)

        return Response(
            {
                'id': company.id
            }, 200
        )
