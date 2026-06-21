# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73424():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
