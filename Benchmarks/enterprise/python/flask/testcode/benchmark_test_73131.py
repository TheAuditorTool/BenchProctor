# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest73131():
    ua_value = request.headers.get('User-Agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    if str(data) not in ('admin', 'user', 'guest', 'viewer'):
        return jsonify({'error': 'forbidden'}), 403
    session['user'] = str(data)
    return jsonify({"result": "success"})
