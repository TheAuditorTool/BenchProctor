# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77217():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
