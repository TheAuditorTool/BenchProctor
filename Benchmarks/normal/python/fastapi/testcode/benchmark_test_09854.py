# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db, auth_check


async def BenchmarkTest09854(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    auth_check('user', data)
    return {"updated": True}
