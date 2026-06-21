# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest24865():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = coalesce_blank(forwarded_ip)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['user'] = str(processed)
    return jsonify({"result": "success"})
