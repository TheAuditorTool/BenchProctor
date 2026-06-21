# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest21945():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
