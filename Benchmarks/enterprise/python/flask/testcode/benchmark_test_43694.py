# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43694():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
