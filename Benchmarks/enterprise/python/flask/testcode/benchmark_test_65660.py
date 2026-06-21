# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify
import json


def BenchmarkTest65660():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
