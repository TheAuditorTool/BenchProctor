# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest23292(request: Request, req: UserInput):
    json_value = req.payload
    if json_value:
        data = json_value
    else:
        data = ''
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
