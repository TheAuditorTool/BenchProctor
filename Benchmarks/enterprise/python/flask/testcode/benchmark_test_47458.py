# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest47458():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    os.chmod('/var/app/data/' + str(comment_value), 0o777)
    return jsonify({"result": "success"})
