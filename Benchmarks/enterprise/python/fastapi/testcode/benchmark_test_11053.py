# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest11053(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
