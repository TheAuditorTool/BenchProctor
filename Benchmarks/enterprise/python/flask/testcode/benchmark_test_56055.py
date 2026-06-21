# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


request_state: dict[str, str] = {}

def BenchmarkTest56055():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
