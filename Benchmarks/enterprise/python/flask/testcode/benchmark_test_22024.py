# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22024():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = forwarded_ip if forwarded_ip else 'default'
    int(str(data))
    return jsonify({"result": "success"})
