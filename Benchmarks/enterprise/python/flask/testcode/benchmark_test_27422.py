# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


def BenchmarkTest27422():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
