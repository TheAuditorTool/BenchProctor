# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


async def BenchmarkTest36682(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % str(db_value)
    globals()['counter'] = int(data)
    return {"updated": True}
