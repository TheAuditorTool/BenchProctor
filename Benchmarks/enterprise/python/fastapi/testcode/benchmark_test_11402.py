# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import base64
from app_runtime import db


async def BenchmarkTest11402(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
