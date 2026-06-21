# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest67937(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    db.execute('SELECT * FROM users WHERE id = ' + str(db_value))
    return {"updated": True}
