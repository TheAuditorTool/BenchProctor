# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14381():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if str(forwarded_ip).startswith(('10.', '192.168.', '127.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
