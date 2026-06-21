# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
from app_runtime import db


async def BenchmarkTest55945(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    requests.get(str(data))
    return {"updated": True}
