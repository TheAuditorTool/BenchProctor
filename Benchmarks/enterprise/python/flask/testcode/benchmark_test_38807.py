# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify
import json


def BenchmarkTest38807():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
