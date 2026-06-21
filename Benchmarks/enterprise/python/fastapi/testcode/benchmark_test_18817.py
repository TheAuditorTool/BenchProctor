# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest18817(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = referer_value
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return {"updated": True}
