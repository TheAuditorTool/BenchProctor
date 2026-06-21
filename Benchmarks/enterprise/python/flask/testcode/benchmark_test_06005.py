# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06005():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if str(forwarded_ip).endswith(('.prod.internal', '.trusted.net')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
