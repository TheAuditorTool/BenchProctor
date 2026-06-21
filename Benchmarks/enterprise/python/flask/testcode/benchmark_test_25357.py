# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest25357():
    header_value = request.headers.get('X-Custom-Header', '')
    digest = hashlib.sha256(str(header_value).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
