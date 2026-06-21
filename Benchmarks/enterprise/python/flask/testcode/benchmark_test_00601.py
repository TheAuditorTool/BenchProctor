# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00601():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
