# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest57667():
    ua_value = request.headers.get('User-Agent', '')
    data = coalesce_blank(ua_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
