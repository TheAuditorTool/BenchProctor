# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72461():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = str(forwarded_ip).replace('\x00', '')
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
