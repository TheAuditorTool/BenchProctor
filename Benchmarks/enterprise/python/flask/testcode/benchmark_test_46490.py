# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest46490():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    auth_check('user', processed)
    return jsonify({"result": "success"})
