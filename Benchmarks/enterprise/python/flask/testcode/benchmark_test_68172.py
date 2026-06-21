# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest68172():
    auth_header = request.headers.get('Authorization', '')
    if not auth_check(session.get('user', ''), str(auth_header)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
