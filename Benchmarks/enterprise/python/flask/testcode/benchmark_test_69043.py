# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


request_state: dict[str, str] = {}

def BenchmarkTest69043():
    upload_name = request.files['upload'].filename
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
