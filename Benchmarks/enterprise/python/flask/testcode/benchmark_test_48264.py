# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest48264():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return jsonify({"result": "success"})
