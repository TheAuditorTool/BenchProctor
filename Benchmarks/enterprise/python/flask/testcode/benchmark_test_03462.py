# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest03462():
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
