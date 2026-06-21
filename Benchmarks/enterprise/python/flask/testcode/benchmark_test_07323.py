# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07323():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
