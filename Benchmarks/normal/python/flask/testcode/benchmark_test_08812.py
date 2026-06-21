# SPDX-License-Identifier: Apache-2.0
import requests
import keyring
from flask import jsonify


def BenchmarkTest08812():
    secret_value = 'app_display_name'
    store_cred = keyring.get_password('app', 'service-account')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(secret_value)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return jsonify({"result": "success"})
