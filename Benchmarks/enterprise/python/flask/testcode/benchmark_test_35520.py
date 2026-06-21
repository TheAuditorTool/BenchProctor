# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest35520():
    header_value = request.headers.get('X-Custom-Header', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(header_value).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
