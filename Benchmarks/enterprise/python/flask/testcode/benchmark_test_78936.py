# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest78936():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
