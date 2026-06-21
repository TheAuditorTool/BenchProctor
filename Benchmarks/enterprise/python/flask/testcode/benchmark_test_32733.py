# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest32733():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return jsonify({"result": "success"})
