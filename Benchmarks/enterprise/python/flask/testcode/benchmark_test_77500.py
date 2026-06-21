# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest77500():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session['data'] = str(data)
    return jsonify({"result": "success"})
