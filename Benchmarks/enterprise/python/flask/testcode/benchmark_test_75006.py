# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest75006():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
