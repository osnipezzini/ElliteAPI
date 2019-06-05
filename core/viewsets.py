# _*_ coding: UTF-8 _*_
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from client.models import Client, Company
from client.serializer import CompanySerializer

'''
Created on 05/06/2019
@author: osnip
'''


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CompanySerializer

    def create(self, request):
        cpf = request.data["cpf"]
        senha = request.data['senha']
        if len(cpf) <= 14:
            client = Client.objects.get(cpf=cpf)
            company = client.company
        else:
            company = Company.objects.get(cnpj=cpf)

        serializer = CompanySerializer(instance=company)
        if check_password(senha, company.password):
            valid_date = serializer.data.get('key').get('valid_date')
            return Response(
                {'key': company.key.key,
                 'valid_date': valid_date,
                 'company': company.name,
                 'server_ip': company.server_ip
                 }, 200
            )
        else:
            return Response({'error': 'Credenciais incorretas'}, 401)
