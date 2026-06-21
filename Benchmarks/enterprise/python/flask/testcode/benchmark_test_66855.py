# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest66855():
    multipart_value = request.form.get('multipart_field', '')
    data = ensure_str(multipart_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
