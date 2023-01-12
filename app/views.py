from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



def verify_password(password, rules):
    all_rules = {}
    no_matche = []


    for var in rules:
        all_rules[var['rule'].lower()] = var['value']

    
    if 'minsize' in all_rules:
        if len(password) < all_rules['minsize']:
            no_matche.append("minsize")
        
     
    if 'minuppercase' in all_rules:
        flag = 0
        for c in password:
            if c.isupper():
                flag += 1
        if flag < all_rules['minuppercase']:
            no_matche.append('minuppercase')


    if 'minlowercase' in all_rules:
        flag = 0
        for c in password:
            if c.islower():
                flag += 1
        if flag < all_rules['minlowercase']:
            no_matche.append('minlowercase')

    


    return all_rules, no_matche




class Validator_Password(APIView):
    """
    Checa se a senha passa em todos os requisitos
    para ser validado.

    """

    def post(self, request):
        password = request.data["password"]
        rules = request.data["rules"]


        if request:
            resposta = f'Está é a senha: {password.upper()}. Essas são as regras: {rules[0]["value"]}'
            print(verify_password(password, rules))

            return Response(resposta, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
            