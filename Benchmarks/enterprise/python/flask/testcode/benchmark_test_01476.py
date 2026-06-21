# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest01476():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
