# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


def BenchmarkTest33724():
    secret_value = 'config_secret_test_abc123'
    if secret_value:
        data = secret_value
    else:
        data = ''
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
