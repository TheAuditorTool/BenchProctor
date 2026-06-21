# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest59632():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = relay_value(db_value)
    return str(data), 200, {'Content-Type': 'text/html'}
