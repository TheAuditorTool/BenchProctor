# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
import json
from app_runtime import auth_check


def BenchmarkTest24644():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
