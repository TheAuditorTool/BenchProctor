# SPDX-License-Identifier: Apache-2.0
from flask import session
import re
from flask import request, jsonify


def BenchmarkTest25133():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
