# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest25256():
    ua_value = request.headers.get('User-Agent', '')
    data = to_text(ua_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
