# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78737():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
