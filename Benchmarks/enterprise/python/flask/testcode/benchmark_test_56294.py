# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56294():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
