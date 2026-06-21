# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest69557(path_param):
    path_value = path_param
    data = unquote(path_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
