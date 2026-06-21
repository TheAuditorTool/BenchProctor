# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest38145():
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})
