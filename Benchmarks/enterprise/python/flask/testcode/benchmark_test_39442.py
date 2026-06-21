# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest39442():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = relay_value(forwarded_ip)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
