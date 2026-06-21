# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest06907():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return jsonify({"result": "success"})
