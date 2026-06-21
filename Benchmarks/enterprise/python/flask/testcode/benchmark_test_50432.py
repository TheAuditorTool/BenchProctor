# SPDX-License-Identifier: Apache-2.0
import logging
import base64
from flask import jsonify
from app_runtime import db


def BenchmarkTest50432():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
