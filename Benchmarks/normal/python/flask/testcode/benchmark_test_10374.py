# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10374():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
