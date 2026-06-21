# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import time


def ensure_str(value):
    return str(value)

def BenchmarkTest65187():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ensure_str(forwarded_ip)
    if time.time() > 1000000000:
        return render_template_string(data)
    return jsonify({"result": "success"})
