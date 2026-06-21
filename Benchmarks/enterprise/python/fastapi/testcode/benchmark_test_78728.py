# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import importlib


def to_text(value):
    return str(value).strip()

async def BenchmarkTest78728(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = to_text(auth_header)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
