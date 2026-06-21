# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52427():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
