# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest12356():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
