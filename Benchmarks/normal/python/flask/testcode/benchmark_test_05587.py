# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest05587():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
