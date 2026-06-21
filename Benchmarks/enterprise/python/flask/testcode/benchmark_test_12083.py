# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest12083():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
