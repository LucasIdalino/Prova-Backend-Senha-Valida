from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



def verify_password(password, rules):
    all_rules = {}
    no_matche = []


    try:
        for var in rules:
            if var == "norepeted":
                all_rules[var['rule'].lower()] = None
            else:
                all_rules[var['rule'].lower()] = var['value']

    except KeyError:
        pass
    

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

    
    if 'mindigit' in all_rules:
        flag = 0
        for c in password:
            if c.isdigit():
                flag += 1
        if flag < all_rules['mindigit']:
            no_matche.append('mindigit')


    if 'minspecialchars' in all_rules:
        chars = []
        for c in password:
            if c.isalnum() == False:
                chars.append(c)
                
        if len(chars) < all_rules['minspecialchars']:
            no_matche.append('minspecialchars')
           
    
    if 'norepeted' in all_rules:
        for c in password:
            if password.count(c) >= 2:
                no_matche.append('norepeated')
                break

    if len(no_matche) == 0:

        res = {
            "verify": True,
            "no_matche": no_matche
        }

    else:
        res = {
            "verify": False,
            "no_matche": no_matche
        }
        
    return res




class Validator_Password(APIView):
    """
    Checa se a senha passa em todos os requisitos
    para ser validado.

    """

    def post(self, request):
        password = request.data["password"]
        rules = request.data["rules"]


        if request:
            resposta = verify_password(password=password, rules=rules)

            return Response(resposta, status=status.HTTP_200_OK)

        else:
            return Response(resposta, status=status.HTTP_204_NO_CONTENT)
            