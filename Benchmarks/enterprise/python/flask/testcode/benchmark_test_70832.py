# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest70832():
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(env_value),))
    return jsonify({"result": "success"})
