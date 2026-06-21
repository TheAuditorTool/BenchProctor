# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57535():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
