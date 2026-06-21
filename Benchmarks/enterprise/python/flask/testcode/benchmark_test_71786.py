# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71786():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
