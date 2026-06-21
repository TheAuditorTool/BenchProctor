# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest48633():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
