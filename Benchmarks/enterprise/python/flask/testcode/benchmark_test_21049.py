# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21049():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
