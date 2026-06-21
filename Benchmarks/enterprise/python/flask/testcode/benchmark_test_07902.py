# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest07902():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = normalise_input(comment_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
