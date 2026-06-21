# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest42227():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % str(db_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return jsonify({"result": "success"})
