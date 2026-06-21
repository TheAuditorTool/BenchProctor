# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest03801():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    return str(data), 200, {'Content-Type': 'text/html'}
