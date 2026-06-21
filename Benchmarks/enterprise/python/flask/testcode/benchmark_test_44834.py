# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest44834():
    upload_name = request.files['upload'].filename
    data = to_text(upload_name)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
