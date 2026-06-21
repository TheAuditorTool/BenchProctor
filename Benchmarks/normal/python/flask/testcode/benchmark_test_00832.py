# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest00832():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = relay_value(json_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
