# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest52209():
    referer_value = request.headers.get('Referer', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(referer_value).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
