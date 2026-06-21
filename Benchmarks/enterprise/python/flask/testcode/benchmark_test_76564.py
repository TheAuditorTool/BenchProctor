# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest76564(path_param):
    path_value = path_param
    if auth_check('user', str(path_value)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
