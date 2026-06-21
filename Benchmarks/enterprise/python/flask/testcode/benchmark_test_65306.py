# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify
from app_runtime import db


def BenchmarkTest65306():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value}'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
