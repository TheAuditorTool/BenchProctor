# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest61131(request: Request, req: UserInput):
    json_value = req.payload
    trusted_claim = str(json_value)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
