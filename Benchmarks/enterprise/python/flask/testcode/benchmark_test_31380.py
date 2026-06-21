# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest31380():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
