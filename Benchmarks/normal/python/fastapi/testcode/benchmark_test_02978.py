# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import importlib


async def BenchmarkTest02978(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = ua_value
    importlib.import_module(str(processed))
    return {"updated": True}
