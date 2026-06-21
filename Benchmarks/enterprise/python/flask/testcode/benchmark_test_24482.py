# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest24482():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})
