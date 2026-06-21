# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest34087():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    auth_check('user', data)
    return jsonify({"result": "success"})
