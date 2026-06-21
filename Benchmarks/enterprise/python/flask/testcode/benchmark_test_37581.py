# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37581():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    eval(str(forwarded_ip))
    return jsonify({"result": "success"})
