# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28583():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
