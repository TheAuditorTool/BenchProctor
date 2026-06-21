# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest21810():
    user_id = request.args.get('id', '')
    if not auth_check(session.get('user', ''), str(user_id)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
