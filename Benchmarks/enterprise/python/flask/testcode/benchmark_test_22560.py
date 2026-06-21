# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest22560(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
