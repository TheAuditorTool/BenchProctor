# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest47357(path_param):
    path_value = path_param
    if not auth_check(str(path_value), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
