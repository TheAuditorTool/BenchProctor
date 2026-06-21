# SPDX-License-Identifier: Apache-2.0
import hashlib
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest11383():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
