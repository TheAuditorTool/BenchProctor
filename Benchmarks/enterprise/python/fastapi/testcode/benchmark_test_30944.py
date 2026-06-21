# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from pydantic import BaseModel
from starlette.responses import JSONResponse
from types import SimpleNamespace


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest30944(request: Request, req: UserInput):
    json_value = req.payload
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
