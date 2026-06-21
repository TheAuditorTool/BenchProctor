# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest75214():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = relay_value(db_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
