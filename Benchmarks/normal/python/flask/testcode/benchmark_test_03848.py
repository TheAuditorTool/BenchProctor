# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest03848():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
