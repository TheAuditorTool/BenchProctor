# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest40571():
    ua_value = request.headers.get('User-Agent', '')
    digest = hashlib.sha1(str(ua_value).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
