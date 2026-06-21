# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest08334():
    raw_body = request.get_data(as_text=True)
    if not auth_check(session.get('user', ''), str(raw_body)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
