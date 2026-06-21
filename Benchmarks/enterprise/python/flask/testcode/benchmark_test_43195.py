# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import jsonify


request_state: dict[str, str] = {}

def BenchmarkTest43195(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
