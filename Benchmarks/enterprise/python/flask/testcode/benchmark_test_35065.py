# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest35065():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    defusedxml.ElementTree.fromstring(str(db_value))
    return jsonify({"result": "success"})
