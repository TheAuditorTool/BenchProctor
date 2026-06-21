# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest13161(path_param):
    path_value = path_param
    data = unquote(path_value)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
