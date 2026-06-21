# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest69507():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session['data'] = str(data)
    return jsonify({"result": "success"})
