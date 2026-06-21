# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest02010():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
