# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from app_runtime import db, auth_check


async def BenchmarkTest34927(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
