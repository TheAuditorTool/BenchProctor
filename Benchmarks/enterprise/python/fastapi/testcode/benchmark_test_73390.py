# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest73390(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
