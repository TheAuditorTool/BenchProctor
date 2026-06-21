# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest80914():
    cookie_value = request.cookies.get('session_token', '')
    random.seed(int(cookie_value) if str(cookie_value).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
