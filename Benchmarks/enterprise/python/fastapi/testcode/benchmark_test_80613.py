# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest80613(request: Request):
    host_value = request.headers.get('host', '')
    if host_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = host_value
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return {"updated": True}
