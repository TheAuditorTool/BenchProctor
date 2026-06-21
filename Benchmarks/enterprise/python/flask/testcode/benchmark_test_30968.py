# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify
from app_runtime import db


def BenchmarkTest30968():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
