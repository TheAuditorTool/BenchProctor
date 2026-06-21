# SPDX-License-Identifier: Apache-2.0
import html
from flask import jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest21034():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
