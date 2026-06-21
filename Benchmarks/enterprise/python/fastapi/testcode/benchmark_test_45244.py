# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import importlib


def relay_value(value):
    return value

async def BenchmarkTest45244(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
