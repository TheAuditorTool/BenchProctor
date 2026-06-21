# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest10122():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(db_value)
    data = collected
    return str(data), 200, {'Content-Type': 'text/html'}
