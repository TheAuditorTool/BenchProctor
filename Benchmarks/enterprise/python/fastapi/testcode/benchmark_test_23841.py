# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest23841(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(raw_body),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
