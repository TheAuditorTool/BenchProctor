# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest18701():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    if session.get('role') != 'admin':
        return jsonify({'error': 'forbidden'}), 403
    session['data'] = str(data)
    return jsonify({"result": "success"})
