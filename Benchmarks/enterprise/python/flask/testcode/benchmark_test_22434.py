# SPDX-License-Identifier: Apache-2.0
import base64
from flask import jsonify
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest22434():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
