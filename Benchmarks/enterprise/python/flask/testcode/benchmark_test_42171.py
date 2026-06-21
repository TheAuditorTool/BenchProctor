# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest42171(path_param):
    path_value = path_param
    data = ensure_str(path_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
