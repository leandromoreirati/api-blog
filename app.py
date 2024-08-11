from requests.auth import HTTPBasicAuth
import requests


# Vamos gerar um token na API e usar esse token para realizar
# autenticação nas rotas protegidas da nossa API
resultado = requests.get('http://localhost:5000/login',
                         auth=('Leandro Moreira', '123456'))

print(resultado.json())

resultado_autores = requests.get('http://localhost:5000/autores',
                                 headers={'x-access-token': resultado.jso()['token']})

print(resultado_autores.json())
