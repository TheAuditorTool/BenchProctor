# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest41738(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
