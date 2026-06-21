# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest22216():
    origin_value = request.headers.get('Origin', '')
    if not auth_check(session.get('user', ''), str(origin_value)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
