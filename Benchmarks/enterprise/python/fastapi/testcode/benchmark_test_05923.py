# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest05923(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
