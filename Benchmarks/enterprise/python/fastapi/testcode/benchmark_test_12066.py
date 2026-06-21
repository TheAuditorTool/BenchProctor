# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest12066(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    if db_value:
        data = db_value
    else:
        data = ''
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
