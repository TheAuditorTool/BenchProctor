# SPDX-License-Identifier: Apache-2.0
import requests
import keyring
from flask import jsonify


def BenchmarkTest78342():
    secret_value = 'default_config_label'
    data = secret_value if secret_value else 'default'
    store_cred = keyring.get_password('app', 'service-account')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return jsonify({"result": "success"})
