# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import jsonify
import time
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest04715():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = default_blank(db_value)
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
