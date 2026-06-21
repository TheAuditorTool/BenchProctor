# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest52414():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
