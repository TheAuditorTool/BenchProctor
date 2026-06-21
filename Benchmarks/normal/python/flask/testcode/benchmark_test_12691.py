# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest12691():
    upload_name = request.files['upload'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
