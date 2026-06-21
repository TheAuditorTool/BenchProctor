# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest24589():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    os.remove(str(data))
    return jsonify({"result": "success"})
