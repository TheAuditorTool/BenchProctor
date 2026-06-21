# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest12103(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    request.session['user'] = str(data)
    return {"updated": True}
