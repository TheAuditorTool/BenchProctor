# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35660():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
