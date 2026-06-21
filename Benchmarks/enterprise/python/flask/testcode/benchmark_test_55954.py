# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55954():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
