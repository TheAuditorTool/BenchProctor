# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import base64
from app_runtime import db, auth_check


async def BenchmarkTest26083(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
