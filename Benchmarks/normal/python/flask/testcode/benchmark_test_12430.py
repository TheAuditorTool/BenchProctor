# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest12430():
    ua_value = request.headers.get('User-Agent', '')
    data = relay_value(ua_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
