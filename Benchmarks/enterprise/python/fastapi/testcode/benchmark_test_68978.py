# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from types import SimpleNamespace


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest68978(request: Request, req: UserInput):
    json_value = req.payload
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})
