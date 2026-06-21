# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest03916(request: Request):
    user_id = request.query_params.get('id', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(user_id),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
