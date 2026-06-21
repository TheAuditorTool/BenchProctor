# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import importlib


async def BenchmarkTest43784(request: Request):
    origin_value = request.headers.get('origin', '')
    if origin_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = origin_value
    importlib.import_module(str(processed))
    return {"updated": True}
