# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55673():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    int(str(forwarded_ip))
    return jsonify({"result": "success"})
