# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23510():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
