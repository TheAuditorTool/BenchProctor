# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest62811(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
