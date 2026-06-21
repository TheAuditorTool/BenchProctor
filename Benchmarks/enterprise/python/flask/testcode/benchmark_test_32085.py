# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from app_runtime import db


def BenchmarkTest32085():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '{}'.format(db_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
