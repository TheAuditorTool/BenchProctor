# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest73830():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
