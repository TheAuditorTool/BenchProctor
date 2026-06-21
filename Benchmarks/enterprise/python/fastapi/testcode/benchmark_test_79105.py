# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest79105(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = coalesce_blank(db_value)
    eval(compile('eval(str(data))', '<sink>', 'exec'))
    return {"updated": True}
