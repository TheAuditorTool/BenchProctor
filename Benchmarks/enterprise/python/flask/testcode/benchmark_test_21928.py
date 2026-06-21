# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest21928():
    origin_value = request.headers.get('Origin', '')
    digest = hashlib.md5(str(origin_value).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
