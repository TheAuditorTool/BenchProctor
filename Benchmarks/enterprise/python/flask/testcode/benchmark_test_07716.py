# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def BenchmarkTest07716(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session['data'] = str(data)
    return jsonify({"result": "success"})
