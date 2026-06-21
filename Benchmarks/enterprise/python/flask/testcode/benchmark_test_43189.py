# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest43189():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
