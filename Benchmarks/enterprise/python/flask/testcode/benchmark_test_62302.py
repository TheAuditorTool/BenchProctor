# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest62302():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
