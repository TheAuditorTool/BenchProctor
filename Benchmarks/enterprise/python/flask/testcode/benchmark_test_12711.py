# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest12711():
    origin_value = request.headers.get('Origin', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(origin_value).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
