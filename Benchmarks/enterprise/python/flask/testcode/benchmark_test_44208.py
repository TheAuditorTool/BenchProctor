# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44208():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
