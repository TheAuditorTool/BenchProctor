# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest02060():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = f'{secret_value}'
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
