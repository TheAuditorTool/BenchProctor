# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02014():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
