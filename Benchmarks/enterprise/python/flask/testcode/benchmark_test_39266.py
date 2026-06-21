# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest39266():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = forwarded_ip if forwarded_ip else 'default'
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
