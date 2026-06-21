# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21881():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
