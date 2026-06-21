# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest06947():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
