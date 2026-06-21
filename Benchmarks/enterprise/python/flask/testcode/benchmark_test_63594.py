# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63594():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    int(str(data))
    return jsonify({"result": "success"})
