# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest03208(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    eval(str(data))
    return {"updated": True}
