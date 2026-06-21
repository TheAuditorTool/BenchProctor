# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import socket


def BenchmarkTest02053():
    referer_value = request.headers.get('Referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    def _primary():
        s = socket.create_connection((str(data), 80))
        s.close()
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
