# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import importlib


async def BenchmarkTest55830(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = header_value
    importlib.import_module(str(processed))
    return {"updated": True}
