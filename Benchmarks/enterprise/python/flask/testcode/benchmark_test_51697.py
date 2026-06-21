# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51697():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    int(str(data))
    return jsonify({"result": "success"})
