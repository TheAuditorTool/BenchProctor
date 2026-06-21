# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest80624():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})
