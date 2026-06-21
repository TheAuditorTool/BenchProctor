# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, auth_check


async def BenchmarkTest09254(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    auth_check('user', data)
    return {"updated": True}
