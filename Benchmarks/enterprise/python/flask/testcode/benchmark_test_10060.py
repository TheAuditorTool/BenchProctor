# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest10060():
    cookie_value = request.cookies.get('session_token', '')
    random.seed(int(cookie_value) if str(cookie_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
