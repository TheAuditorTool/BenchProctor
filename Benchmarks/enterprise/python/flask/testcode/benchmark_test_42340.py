# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def relay_value(value):
    return value

def BenchmarkTest42340():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
