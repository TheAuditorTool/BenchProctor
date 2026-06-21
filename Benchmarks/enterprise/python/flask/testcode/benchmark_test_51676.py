# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


def BenchmarkTest51676():
    field_value = request.form.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return jsonify({"result": "success"})
