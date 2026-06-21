# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest52962():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
