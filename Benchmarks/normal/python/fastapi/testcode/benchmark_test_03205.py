# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from app_runtime import db


async def BenchmarkTest03205(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
