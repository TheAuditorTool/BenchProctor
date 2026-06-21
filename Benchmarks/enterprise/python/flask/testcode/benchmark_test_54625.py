# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest54625():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
