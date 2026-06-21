# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest62591():
    field_value = request.form.get('field', '')
    data = default_blank(field_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
