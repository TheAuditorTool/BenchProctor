# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest12332():
    ua_value = request.headers.get('User-Agent', '')
    auth_check('user', hashlib.sha256(str(ua_value).encode()).hexdigest())
    return jsonify({"result": "success"})
