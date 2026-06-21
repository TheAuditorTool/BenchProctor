# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60180():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    if str(data).startswith(('10.', '192.168.', '127.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
