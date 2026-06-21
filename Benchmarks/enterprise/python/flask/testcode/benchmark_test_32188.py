# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


def relay_value(value):
    return value

def BenchmarkTest32188():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = relay_value(forwarded_ip)
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
