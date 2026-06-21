# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest49739():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
