# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest78863():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = forwarded_ip if forwarded_ip else 'default'
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
