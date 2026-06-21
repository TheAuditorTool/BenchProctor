# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest66487():
    env_value = os.environ.get('USER_INPUT', '')
    if not auth_check(session.get('user', ''), str(env_value)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
