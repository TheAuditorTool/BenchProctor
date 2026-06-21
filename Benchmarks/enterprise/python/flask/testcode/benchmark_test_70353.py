# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import time
from app_runtime import db


def BenchmarkTest70353():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
