# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79384():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
