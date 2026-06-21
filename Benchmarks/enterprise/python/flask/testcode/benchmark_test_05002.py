# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05002():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
