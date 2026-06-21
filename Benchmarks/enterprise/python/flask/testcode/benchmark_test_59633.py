# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59633():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
