# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


request_state: dict[str, str] = {}

def BenchmarkTest38124():
    multipart_value = request.form.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
