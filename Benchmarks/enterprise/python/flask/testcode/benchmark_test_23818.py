# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest23818():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = handle(comment_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
