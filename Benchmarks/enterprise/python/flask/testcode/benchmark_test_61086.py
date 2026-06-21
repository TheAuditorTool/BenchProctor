# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest61086():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
