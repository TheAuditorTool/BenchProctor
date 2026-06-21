# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify
from app_runtime import db


def BenchmarkTest19107():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
