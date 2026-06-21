# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from app_runtime import db


def BenchmarkTest24250():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    logging.info('User action: ' + str(db_value))
    return jsonify({"result": "success"})
