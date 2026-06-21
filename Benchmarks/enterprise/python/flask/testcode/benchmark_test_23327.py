# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify
from app_runtime import db


def BenchmarkTest23327():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '{}'.format(db_value)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
