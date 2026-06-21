# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import importlib


async def BenchmarkTest46197(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = forwarded_ip
    importlib.import_module(str(processed))
    return {"updated": True}
