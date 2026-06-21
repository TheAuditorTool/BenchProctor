# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest09952():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    kind = 'json' if str(comment_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = comment_value
            data = parsed
        case _:
            data = comment_value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
