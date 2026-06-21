# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def relay_value(value):
    return value

def BenchmarkTest34786():
    referer_value = request.headers.get('Referer', '')
    data = relay_value(referer_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
