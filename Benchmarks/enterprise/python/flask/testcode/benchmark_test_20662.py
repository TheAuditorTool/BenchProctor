# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from app_runtime import db


def BenchmarkTest20662():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    logging.info('User action: ' + str(comment_value))
    return jsonify({"result": "success"})
