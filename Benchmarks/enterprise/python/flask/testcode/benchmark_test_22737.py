# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from app_runtime import db


def BenchmarkTest22737():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % (comment_value,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
