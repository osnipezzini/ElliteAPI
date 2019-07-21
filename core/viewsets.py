# _*_ coding: UTF-8 _*_
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from client.models import Client, Company
from client.serializer import CompanySerializer
from core.utils import Crypto
from key.models import Key
from key.serializer import KeySerializer

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
        machine = request.data['machine']
        if len(cpf) <= 14:
            if len(Client.objects.filter(cpf=cpf)) > 0:
                client = Client.objects.get(cpf=cpf)
                company = client.company
            else:
                return Response({'error': 'Dados incorretos !'}, 401)
        else:
            if len(Company.objects.filter(cnpj=cpf)) > 0:
                company = Company.objects.get(cnpj=cpf)
            else:
                return Response({'error': 'Dados incorretos !'}, 401)
        try:
            check_password(senha, company.password)
            keys = company.keys.filter(machine=machine)
            if len(keys) <= 0:
                key = Crypto(cpf)
                key.encrypt()
                serial = key.generate_serial()
                key_model = Key(key=serial, machine=machine)
                key_model.save()
                company.keys.add(key_model)
            else:
                key_model = company.keys.get(machine=machine)

            return Response(
                {'key': key_model.key,
                 'valid_date': key_model.valid_date.strftime("%d/%m/%Y"),
                 'company': company.name,
                 'server_ip': company.server_ip
                 }, 200)
        except Exception as e:
            print(e)
            return Response({'error': 'Dados incorretos !'}, 401)
