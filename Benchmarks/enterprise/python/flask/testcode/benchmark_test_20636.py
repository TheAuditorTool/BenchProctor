# SPDX-License-Identifier: Apache-2.0
import random
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest20636():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
