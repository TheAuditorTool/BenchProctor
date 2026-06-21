# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import subprocess
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest60454():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = relay_value(db_value)
    def _primary():
        subprocess.run([str(data), '--status'], shell=False)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
