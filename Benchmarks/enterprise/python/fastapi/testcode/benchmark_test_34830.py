# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db, auth_check


async def BenchmarkTest34830(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(db_value), store_cred)
    return {"updated": True}
