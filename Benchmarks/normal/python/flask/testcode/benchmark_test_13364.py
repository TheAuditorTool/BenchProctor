# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest13364():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
