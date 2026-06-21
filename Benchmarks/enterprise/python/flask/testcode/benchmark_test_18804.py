# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest18804():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
