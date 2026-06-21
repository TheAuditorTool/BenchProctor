# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest06629(request: Request, req: UserInput):
    json_value = req.payload
    request.session['data'] = str(json_value)
    return {"updated": True}
