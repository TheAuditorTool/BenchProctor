# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import jsonify
import time
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest09228():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
