# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


request_state: dict[str, str] = {}

def BenchmarkTest10819():
    field_value = request.form.get('field', '')
    request_state['last_input'] = field_value
    data = request_state['last_input']
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
