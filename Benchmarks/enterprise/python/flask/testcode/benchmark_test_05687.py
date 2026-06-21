# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest05687():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    return str(data), 200, {'Content-Type': 'text/html'}
