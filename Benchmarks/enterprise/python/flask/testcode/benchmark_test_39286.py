# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify
from app_runtime import db


def BenchmarkTest39286():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
