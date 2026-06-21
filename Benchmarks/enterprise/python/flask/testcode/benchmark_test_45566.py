# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest45566():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = to_text(forwarded_ip)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return jsonify({"result": "success"})
