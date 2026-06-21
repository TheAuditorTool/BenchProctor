# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest72775():
    ua_value = request.headers.get('User-Agent', '')
    digest = str(ua_value).encode().hex()
    return jsonify({'digest': str(digest)}), 200
