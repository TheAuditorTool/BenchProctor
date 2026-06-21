# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest44433():
    upload_name = request.files['upload'].filename
    if not auth_check(session.get('user', ''), str(upload_name)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
