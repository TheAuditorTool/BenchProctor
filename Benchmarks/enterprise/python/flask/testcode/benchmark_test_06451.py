# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest06451():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
