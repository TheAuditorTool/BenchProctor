# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db, auth_check


async def BenchmarkTest05487(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    auth_check('user', data)
    return {"updated": True}
