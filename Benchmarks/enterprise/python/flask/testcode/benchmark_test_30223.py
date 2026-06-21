# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest30223():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
