# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest57650():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
