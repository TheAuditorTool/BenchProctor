# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest07473():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
