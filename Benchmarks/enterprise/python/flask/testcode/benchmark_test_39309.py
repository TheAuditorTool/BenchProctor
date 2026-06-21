# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import db


def BenchmarkTest39309():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    kind = 'json' if str(comment_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = comment_value
            data = parsed
        case _:
            data = comment_value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
