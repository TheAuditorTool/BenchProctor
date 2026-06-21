# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44688():
    header_value = request.headers.get('X-Custom-Header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
