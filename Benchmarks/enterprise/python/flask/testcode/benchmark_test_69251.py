# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest69251():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
