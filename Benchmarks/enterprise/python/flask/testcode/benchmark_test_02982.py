# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from app_runtime import db


def BenchmarkTest02982():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
