# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest58452():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
