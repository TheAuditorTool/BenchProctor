# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest26779(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    request.session['user'] = str(data)
    return {"updated": True}
