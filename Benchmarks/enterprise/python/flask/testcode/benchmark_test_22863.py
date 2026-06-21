# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import db


def BenchmarkTest22863():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    json.loads(data)
    return jsonify({"result": "success"})
