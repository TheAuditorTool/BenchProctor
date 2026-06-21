# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest24102():
    multipart_value = request.form.get('multipart_field', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(multipart_value).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
