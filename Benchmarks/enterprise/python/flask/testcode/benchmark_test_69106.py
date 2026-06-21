# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest69106():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    pending = list(str(db_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
