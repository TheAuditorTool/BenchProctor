# SPDX-License-Identifier: Apache-2.0
import subprocess
import shlex
from flask import jsonify
from app_runtime import db


def BenchmarkTest57102():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
