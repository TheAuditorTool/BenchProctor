# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest17715(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
