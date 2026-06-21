# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest66256(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = relay_value(db_value)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
