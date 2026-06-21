# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest65656():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
