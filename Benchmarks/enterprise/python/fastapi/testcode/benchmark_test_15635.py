# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest15635(request: Request, req: UserInput):
    json_value = req.payload
    raise RuntimeError('processing failed: ' + str(json_value))
    return {"updated": True}
