# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest34095(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return jsonify({"result": "success"})
