# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def BenchmarkTest01291():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
