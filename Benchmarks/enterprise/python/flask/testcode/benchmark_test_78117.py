# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest78117():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
