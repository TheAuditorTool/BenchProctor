# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest11114(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return JSONResponse({'error': str(comment_value), 'stack': repr(locals())}, status_code=500)
