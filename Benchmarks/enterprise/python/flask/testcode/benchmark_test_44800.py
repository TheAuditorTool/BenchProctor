# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest44800():
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return jsonify({"result": "success"})
