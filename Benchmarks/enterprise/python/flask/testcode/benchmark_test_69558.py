# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest69558(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})
