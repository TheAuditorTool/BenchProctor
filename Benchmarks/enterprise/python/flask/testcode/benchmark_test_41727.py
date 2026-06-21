# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest41727(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
