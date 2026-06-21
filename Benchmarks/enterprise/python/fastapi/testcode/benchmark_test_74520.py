# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest74520(request: Request, req: UserInput):
    json_value = req.payload
    if json_value:
        data = json_value
    else:
        data = ''
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
