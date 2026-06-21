# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest46040():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
