# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66985():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
