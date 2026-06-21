# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest20701():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
