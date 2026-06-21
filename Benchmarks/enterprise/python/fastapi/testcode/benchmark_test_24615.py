# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest24615(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    processed = data[:64]
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})
