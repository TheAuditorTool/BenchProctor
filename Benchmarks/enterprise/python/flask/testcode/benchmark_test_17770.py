# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest17770():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})
