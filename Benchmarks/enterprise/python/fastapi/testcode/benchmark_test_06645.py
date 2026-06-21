# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest06645(request: Request, req: UserInput):
    json_value = req.payload
    parts = str(json_value).split(',')
    data = ','.join(parts)
    request.session['user'] = str(data)
    return {"updated": True}
