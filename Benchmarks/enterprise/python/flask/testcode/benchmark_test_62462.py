# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62462():
    host_value = request.headers.get('Host', '')
    globals().setdefault('_secret_cache', {})['current'] = str(host_value)
    return jsonify({"result": "success"})
