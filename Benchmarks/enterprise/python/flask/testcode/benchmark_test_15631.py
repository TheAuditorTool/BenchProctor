# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15631():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
