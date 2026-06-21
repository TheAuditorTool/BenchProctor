# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest06897():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = ensure_str(json_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
