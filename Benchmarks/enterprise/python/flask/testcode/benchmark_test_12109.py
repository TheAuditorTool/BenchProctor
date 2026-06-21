# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest12109():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session['data'] = str(data)
    return jsonify({"result": "success"})
