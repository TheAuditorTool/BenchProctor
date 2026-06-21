# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest11382():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
