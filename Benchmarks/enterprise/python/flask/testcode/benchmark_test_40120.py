# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
from app_runtime import db


def BenchmarkTest40120():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return jsonify({"result": "success"})
