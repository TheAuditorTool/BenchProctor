# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02496():
    host_value = request.headers.get('Host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
