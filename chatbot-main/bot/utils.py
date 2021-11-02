import json

import pycep_correios
import requests
from pycep_correios import get_address_from_cep, WebService


def consulta_cep(cep):
    try:
        request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
        address_data = request.json()
        return address_data
    except Exception as e:
        return request