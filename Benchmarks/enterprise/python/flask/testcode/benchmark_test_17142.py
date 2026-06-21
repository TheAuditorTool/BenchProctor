# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import jsonify
import time
from app_runtime import db


def BenchmarkTest17142():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(db_value)
    data = collected
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
