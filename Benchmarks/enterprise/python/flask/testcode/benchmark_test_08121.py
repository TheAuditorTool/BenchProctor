# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest08121():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    auth_check('user', data)
    return jsonify({"result": "success"})
