# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest21171():
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
