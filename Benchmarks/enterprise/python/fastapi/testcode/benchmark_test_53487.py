# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest53487(request: Request, req: UserInput):
    json_value = req.payload
    digest = hashlib.md5(str(json_value).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
