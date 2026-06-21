# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest14944():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    os.seteuid(65534)
    return jsonify({"result": "success"})
