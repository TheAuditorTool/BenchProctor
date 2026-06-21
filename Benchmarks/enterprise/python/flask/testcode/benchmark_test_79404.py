# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest79404(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
