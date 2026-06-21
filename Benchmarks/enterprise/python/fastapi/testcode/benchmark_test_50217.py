# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest50217(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
