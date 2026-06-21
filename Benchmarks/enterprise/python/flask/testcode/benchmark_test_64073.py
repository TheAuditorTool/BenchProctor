# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest64073():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    return str(data), 200, {'Content-Type': 'text/html'}
