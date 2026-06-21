# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest27535(path_param):
    path_value = path_param
    auth_check('user', path_value)
    return jsonify({"result": "success"})
