# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest61016():
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('SELECT * FROM "' + str(env_value).replace('"', '""') + '"')
    return jsonify({"result": "success"})
