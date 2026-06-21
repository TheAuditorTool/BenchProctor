# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest45860(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
