# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest75495(path_param):
    path_value = path_param
    if not auth_check(session.get('user', ''), str(path_value)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
