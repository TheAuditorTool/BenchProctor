# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess
from app_runtime import db


def BenchmarkTest24020():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    subprocess.run([str(db_value), '--status'], shell=False)
    return jsonify({"result": "success"})
