# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify
from app_runtime import db


def BenchmarkTest69977():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ','.join(parts)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
