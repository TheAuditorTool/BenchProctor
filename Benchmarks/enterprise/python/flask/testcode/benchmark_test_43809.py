# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest43809():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
