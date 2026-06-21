# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest23522():
    auth_header = request.headers.get('Authorization', '')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(auth_header)
    return jsonify({"result": "success"})
