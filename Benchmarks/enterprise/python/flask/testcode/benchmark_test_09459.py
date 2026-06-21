# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import time


def BenchmarkTest09459():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    if time.time() > 1000000000:
        return render_template_string(data)
    return jsonify({"result": "success"})
