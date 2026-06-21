# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest80697(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
