# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest03852():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
