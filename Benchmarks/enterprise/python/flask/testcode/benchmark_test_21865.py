# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest21865():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = coalesce_blank(json_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
