# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29954():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
