# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest73820(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
