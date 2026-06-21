# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07549():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    raise RuntimeError('processing failed: ' + str(forwarded_ip))
    return jsonify({"result": "success"})
