# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest18134():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
