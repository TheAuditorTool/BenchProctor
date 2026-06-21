# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29415():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
