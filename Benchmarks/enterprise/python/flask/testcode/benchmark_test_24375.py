# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest24375():
    host_value = request.headers.get('Host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
