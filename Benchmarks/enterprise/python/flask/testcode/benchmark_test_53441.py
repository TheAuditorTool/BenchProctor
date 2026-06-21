# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest53441():
    upload_name = request.files['upload'].filename
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
