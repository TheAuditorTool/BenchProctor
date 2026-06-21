# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest37574(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    return HTMLResponse(str(data))
