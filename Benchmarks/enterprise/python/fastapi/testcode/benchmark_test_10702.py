# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from app_runtime import db


async def BenchmarkTest10702(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    os.seteuid(65534)
    return {"updated": True}
