# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
import importlib


async def BenchmarkTest07269(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = env_value
    importlib.import_module(str(processed))
    return {"updated": True}
