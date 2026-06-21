# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24529():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
