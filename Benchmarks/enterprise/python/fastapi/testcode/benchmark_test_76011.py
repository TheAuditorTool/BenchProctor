# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
def ensure_str(value):
    return str(value)

async def BenchmarkTest76011(request: Request, req: UserInput):
    json_value = req.payload
    data = ensure_str(json_value)
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
