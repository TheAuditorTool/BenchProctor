# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import db


def BenchmarkTest07295():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with open('/var/uploads/' + str(comment_value), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
