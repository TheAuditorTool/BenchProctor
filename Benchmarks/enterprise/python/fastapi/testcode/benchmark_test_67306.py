# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest67306(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
