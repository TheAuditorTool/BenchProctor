# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest58747():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    auth_check('user', data)
    return jsonify({"result": "success"})
