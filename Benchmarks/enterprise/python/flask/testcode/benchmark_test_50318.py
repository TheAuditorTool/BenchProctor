# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest50318():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
