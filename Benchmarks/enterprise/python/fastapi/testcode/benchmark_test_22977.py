# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest22977(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = path_value
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return {"updated": True}
