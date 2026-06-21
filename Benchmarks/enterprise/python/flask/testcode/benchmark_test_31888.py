# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31888():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % str(json_value)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
