# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest73334():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = to_text(forwarded_ip)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
