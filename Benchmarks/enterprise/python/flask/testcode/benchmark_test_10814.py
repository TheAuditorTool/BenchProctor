# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import db


def BenchmarkTest10814():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = str(db_value).replace('\x00', '')
    yaml.safe_load(data)
    return jsonify({"result": "success"})
