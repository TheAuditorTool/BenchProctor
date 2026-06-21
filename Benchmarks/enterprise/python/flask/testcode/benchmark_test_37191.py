# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest37191():
    header_value = request.headers.get('X-Custom-Header', '')
    globals()['counter'] = int(header_value)
    return jsonify({"result": "success"})
