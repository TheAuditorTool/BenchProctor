# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest22208():
    field_value = request.form.get('field', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(field_value).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
