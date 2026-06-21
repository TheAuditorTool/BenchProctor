# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest49406():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    if os.environ.get("APP_ENV", "production") != "test":
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
