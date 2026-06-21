# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest74049():
    upload_name = request.files['upload'].filename
    digest = hashlib.pbkdf2_hmac('sha256', str(upload_name).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
