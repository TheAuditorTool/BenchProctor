# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest03710(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
