# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import json
from app_runtime import db


async def BenchmarkTest76856(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    return HTMLResponse('<div>' + str(data) + '</div>')
