# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest37180():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    auth_check('user', data)
    return jsonify({"result": "success"})
