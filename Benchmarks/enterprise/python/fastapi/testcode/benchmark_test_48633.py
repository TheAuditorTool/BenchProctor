# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
request_state: dict[str, str] = {}

async def BenchmarkTest48633(request: Request, req: UserInput):
    json_value = req.payload
    request_state['last_input'] = json_value
    data = request_state['last_input']
    if str(data).endswith(('/public', '/static', '/.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
