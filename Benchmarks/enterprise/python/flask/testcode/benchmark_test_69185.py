# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest69185():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    requests.get(str(db_value))
    return jsonify({"result": "success"})
