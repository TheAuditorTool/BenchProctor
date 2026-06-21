# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest54303():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
