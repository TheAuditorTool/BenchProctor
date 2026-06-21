# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest31367():
    upload_name = request.files['upload'].filename
    data = default_blank(upload_name)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
