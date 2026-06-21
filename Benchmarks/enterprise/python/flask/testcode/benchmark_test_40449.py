# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest40449():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    auth_check('user', data)
    return jsonify({"result": "success"})
