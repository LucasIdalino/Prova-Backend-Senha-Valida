# Validator Password API

API REST para checar se a senha passa em todos os requisitos para ser validado.

-----------

## Como executar:

 - Clone o repositório e entre na pasta.
 
`$ git clone https://github.com/LucasIdalino/Prova-Backend-Senha-Valida.git`

  - Crie um ambiente virtual e ative o
  
`$ python -m venv venv`

`$ source venv/bin/activate` ou `venv/Scripts/activate`

  - No terminal, instale os requerimentos
  
`pip install -r requirements.txt`

  - Por último, execute a aplicação
  
`py manage.py runserver`

  - Após iniciar a aplicação acesse o link: `http://127.0.0.1:8000/app/verify/`

  - No campo "Content", coloque a senha e as regras, em JSON para verificar.
  
`{
  "password": "TesteSenhaForte!123&",
  "rules": [
    {"rule": "minSize","value": 8},
    {"rule": "minSpecialChars","value": 2},
    {"rule": "noRepeted","value": 0},
    {"rule": "minDigit","value": 4}
  ]
}`

  - A respota deverá ser algo como isso
`{
"verify": false,
"noMatch": ["minDigit"]
}`

  - Caso sua senha passe nas regras, verify retornará `True` e noMatch retornará uma lista vazia.
