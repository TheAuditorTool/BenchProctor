# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import jsonify
import time
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest12968():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        return render_template_string(data)
    return jsonify({"result": "success"})
