# SPDX-License-Identifier: Apache-2.0
import requests
import keyring
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest25663():
    secret_value = 'app_display_name'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    store_cred = keyring.get_password('app', 'service-account')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return jsonify({"result": "success"})
