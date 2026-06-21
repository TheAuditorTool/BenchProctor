# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest08444(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    auth_check('user', data)
    return jsonify({"result": "success"})
