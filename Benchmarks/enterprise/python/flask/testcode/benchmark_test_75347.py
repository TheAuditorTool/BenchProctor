# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest75347():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    pending = list(str(comment_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
