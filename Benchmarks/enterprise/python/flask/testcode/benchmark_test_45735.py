# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest45735():
    user_id = request.args.get('id', '')
    data = ensure_str(user_id)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
