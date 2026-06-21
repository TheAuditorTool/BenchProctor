# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest01825():
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
