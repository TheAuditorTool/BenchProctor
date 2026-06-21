# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest16298(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(comment_value))
    return resp
