# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest73402():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})
