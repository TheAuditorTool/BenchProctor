# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest05782():
    upload_name = request.files['upload'].filename
    data = relay_value(upload_name)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
