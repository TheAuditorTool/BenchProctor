# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import db


def BenchmarkTest10107():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    yaml.safe_load(db_value)
    return jsonify({"result": "success"})
