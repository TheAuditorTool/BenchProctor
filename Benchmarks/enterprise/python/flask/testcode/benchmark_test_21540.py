# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest21540():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    auth_check('user', hashlib.sha256(str(forwarded_ip).encode()).hexdigest())
    return jsonify({"result": "success"})
