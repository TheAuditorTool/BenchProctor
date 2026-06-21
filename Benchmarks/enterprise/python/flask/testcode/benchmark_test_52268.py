# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest52268():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
