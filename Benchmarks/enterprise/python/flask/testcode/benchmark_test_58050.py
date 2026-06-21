# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58050():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
