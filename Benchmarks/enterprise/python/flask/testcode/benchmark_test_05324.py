# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import time
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest05324():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
