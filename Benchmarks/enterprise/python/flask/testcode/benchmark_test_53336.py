# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest53336():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
