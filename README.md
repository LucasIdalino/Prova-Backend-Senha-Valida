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
 
 ----------
 
 ## Lógica de Implementação
 
 **Toda lógica de implementação está contida no arquivo** `app\views.py`.
 
 Na regra de negócio, o script vai primeiro identificar as regras passadas na entrada para que assim sejam executadas.
 
 Na linha 13 o loop `for var in rules:`, identificará as regras.
 
 Com as regras identificadas, as `if` conditions irá checar as regras e valores guardadas no dicionário `all_rules`. 
 
 A cada `if` analisado, iteradores vão analisar se a senha passa em todas as regras. Caso a senha não passe, a regra não respeitada será guardada em uma lista chamada `no_match`. 
 
 Para a saída da API, caso `no_match` esteja vazio ou não, a API retornará uma resposta em formato JSON:
 
 `{
   "verify": True,
   "no_match": []
  }`
 
 `{
   "verify": False,
   "no_match": ["minsize"]
  }`
 
