# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest59954():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
