# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def BenchmarkTest57968(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
