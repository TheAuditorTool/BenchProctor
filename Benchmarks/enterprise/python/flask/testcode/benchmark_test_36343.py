# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest36343():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session['data'] = str(data)
    return jsonify({"result": "success"})
