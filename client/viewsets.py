# _*_ coding: UTF-8 _*_

'''
Created on 05/06/2019
@author: osnip
'''
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from client.models import Company


class CompanyViewSet(viewsets.ViewSet):
    queryset = Company.objects.all()
    permission_classes = (AllowAny,)

    def retrieve(self, request, pk):
        company = Company.objects.get(pk=pk)
        serializer_class = CompanySerializer

    def create(self, request):
        cpf = request.data["cnpj"]
        senha = request.data['senha']
        server_ip = request.data['server_ip']
        name = request.data['name']

        password = make_password(senha)
        company = Company.objects.create(cnpj=cpf, name=name, server_ip=server_ip, password=password)

        return Response(
            {
                'id': company.id,
                'senha': password
            }, 200
        )
