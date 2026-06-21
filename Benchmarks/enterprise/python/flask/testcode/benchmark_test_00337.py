# SPDX-License-Identifier: Apache-2.0
import os
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest00337():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    os.remove(str(data))
    return jsonify({"result": "success"})
