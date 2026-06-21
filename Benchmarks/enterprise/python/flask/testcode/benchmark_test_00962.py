# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest00962():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})
