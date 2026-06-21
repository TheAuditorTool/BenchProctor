# SPDX-License-Identifier: Apache-2.0
from app_runtime import db


def BenchmarkTest65125():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    pending = list(str(db_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return str(data), 200, {'Content-Type': 'text/html'}
