# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest44026(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    auth_check('user', data)
    return jsonify({"result": "success"})
