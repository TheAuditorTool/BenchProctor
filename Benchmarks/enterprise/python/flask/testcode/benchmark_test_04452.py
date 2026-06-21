# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04452():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
