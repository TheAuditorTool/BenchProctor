# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest29165():
    cookie_value = request.cookies.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
