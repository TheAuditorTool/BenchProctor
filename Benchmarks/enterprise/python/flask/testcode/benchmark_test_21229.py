# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest21229():
    raw_body = request.get_data(as_text=True)
    data = coalesce_blank(raw_body)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return jsonify({'digest': str(digest)}), 200
