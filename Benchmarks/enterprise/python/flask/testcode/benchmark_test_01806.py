# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest01806():
    ua_value = request.headers.get('User-Agent', '')
    if session.get('role') != 'admin':
        return jsonify({'error': 'forbidden'}), 403
    session['data'] = str(ua_value)
    return jsonify({"result": "success"})
