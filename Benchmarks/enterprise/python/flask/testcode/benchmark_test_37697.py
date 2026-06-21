# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest37697():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
