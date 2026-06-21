# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest25386():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
