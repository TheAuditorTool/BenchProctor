# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest03313():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = coalesce_blank(db_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
