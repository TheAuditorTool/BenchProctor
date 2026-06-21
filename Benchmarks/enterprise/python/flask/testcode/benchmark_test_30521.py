# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest30521():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return jsonify({"result": "success"})
