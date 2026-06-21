# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import importlib


async def BenchmarkTest39994(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = user_id
    importlib.import_module(str(processed))
    return {"updated": True}
