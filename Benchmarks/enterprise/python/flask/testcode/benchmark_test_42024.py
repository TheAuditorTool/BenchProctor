# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest42024():
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(env_value),))
    return jsonify({"result": "success"})
