# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55064():
    cookie_value = request.cookies.get('session_token', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(cookie_value))
    return jsonify({'lookup': arr[idx]}), 200
