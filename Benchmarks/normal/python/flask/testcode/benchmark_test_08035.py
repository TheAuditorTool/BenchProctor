# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest08035():
    ua_value = request.headers.get('User-Agent', '')
    reader = make_reader(ua_value)
    data = reader()
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
