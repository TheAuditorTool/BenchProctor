# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest55319(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value:.200s}'
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
