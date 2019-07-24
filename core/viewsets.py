# _*_ coding: UTF-8 _*_
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from client.models import Client, Company
from client.serializer import CompanySerializer
from core.utils import Crypto
from key.models import Key

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
        product = request.data['product']
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
            products = company.product.filter(product_type=product)
            keys = Key.objects.filter(machine=machine)
            if len(products) == 0:
                print(product)
                return Response({'error': 'Cliente não possui produto cadastrado !'}, 401)
            else:
                if len(keys) <= 0:
                    key = Crypto(machine)
                    key.encrypt()
                    serial = key.generate_serial()
                    key_model = Key(key=serial, machine=machine)
                    key_model.save()
                    company.product.keys.add(key_model)
                else:
                    key_model = Key.objects.get(machine=machine)

            return Response(
                {'key': key_model.key,
                 'valid_date': key_model.valid_date.strftime("%d/%m/%Y"),
                 'company': company.name,
                 'server_ip': company.server_ip,
                 'company_logo': company.get_logo_url()
                 }, 200)
        except Exception as e:
            print(e)
            return Response({'error': 'Dados incorretos !'}, 401)
