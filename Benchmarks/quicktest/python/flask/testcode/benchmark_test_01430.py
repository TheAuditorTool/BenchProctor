# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify
from app_runtime import db


def BenchmarkTest01430():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    pending = list(str(db_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
