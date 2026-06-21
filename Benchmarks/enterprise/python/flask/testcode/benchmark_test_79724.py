# SPDX-License-Identifier: Apache-2.0
import hashlib
from urllib.parse import unquote
from flask import request, jsonify
import os


def BenchmarkTest79724():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
