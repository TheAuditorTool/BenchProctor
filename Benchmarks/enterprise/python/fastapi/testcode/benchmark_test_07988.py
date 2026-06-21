# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest07988(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    request.session['data'] = str(data)
    return {"updated": True}
