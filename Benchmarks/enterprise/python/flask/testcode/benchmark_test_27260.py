# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify


def BenchmarkTest27260():
    env_value = os.environ.get('USER_INPUT', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(env_value).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
