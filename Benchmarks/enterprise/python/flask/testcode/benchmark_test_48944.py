# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def BenchmarkTest48944():
    host_value = request.headers.get('Host', '')
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
