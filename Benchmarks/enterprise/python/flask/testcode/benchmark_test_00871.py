# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest00871():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
