# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import json
from app_runtime import auth_check


def BenchmarkTest06698():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
