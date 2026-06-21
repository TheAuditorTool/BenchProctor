# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest67963():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})
