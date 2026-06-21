# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest03098():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
