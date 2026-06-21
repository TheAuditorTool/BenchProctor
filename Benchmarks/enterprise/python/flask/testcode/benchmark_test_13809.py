# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest13809():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})
