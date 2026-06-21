# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest30187():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
