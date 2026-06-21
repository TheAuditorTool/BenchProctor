# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68094():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
