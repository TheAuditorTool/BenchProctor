# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from app_runtime import db


def BenchmarkTest49131():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
