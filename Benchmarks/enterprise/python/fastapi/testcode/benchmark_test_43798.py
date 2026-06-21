# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest43798(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    eval(str(data))
    return {"updated": True}
