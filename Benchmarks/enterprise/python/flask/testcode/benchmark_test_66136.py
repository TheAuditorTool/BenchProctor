# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest66136():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    os.remove(str(comment_value))
    return jsonify({"result": "success"})
