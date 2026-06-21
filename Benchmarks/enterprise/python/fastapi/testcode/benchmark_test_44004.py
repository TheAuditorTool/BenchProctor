# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest44004(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    return HTMLResponse(str(data))
