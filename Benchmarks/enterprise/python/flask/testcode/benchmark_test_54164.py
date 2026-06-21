# SPDX-License-Identifier: Apache-2.0
import random
import base64
from flask import request, jsonify


def BenchmarkTest54164():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
