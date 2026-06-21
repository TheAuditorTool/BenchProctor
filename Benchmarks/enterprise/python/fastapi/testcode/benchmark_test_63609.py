# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest63609(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
