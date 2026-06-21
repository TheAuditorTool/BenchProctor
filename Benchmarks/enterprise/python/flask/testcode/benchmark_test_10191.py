# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest10191():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
