# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


def BenchmarkTest35215():
    host_value = request.headers.get('Host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
