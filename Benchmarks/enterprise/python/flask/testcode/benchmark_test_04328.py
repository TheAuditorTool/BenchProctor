# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import time
import subprocess
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest04328():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = to_text(db_value)
    if time.time() > 1000000000:
        subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
