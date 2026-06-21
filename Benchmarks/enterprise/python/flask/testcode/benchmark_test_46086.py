# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest46086():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
