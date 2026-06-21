# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21028():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
