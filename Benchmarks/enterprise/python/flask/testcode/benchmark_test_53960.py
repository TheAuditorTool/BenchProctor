# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53960():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
