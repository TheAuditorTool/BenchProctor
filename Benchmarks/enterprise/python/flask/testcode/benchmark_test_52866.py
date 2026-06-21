# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest52866():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
