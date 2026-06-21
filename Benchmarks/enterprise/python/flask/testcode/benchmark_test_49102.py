# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest49102():
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    data = bytearray(int(processed) if str(processed).isdigit() else 0)
    return jsonify({"result": "success"})
