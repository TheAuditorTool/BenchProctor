# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest17283():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    os.system('echo ' + str(comment_value))
    return jsonify({"result": "success"})
