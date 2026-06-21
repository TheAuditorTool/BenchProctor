# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def BenchmarkTest62006():
    user_id = request.args.get('id', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(user_id).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
