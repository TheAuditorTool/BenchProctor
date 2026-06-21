# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest72100():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    session['data'] = str(data)
    return jsonify({"result": "success"})
