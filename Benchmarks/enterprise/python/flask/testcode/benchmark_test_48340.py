# SPDX-License-Identifier: Apache-2.0
import json
import requests
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest48340():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    request_state['last_input'] = api_value
    data = request_state['last_input']
    json.loads(data)
    return jsonify({"result": "success"})
