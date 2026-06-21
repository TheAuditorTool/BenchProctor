# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28727():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
