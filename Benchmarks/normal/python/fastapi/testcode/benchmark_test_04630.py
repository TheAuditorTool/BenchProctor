# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest04630(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
