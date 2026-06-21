# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest74956():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
