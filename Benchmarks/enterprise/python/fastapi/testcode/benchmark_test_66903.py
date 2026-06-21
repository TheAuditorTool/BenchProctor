# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest66903(request: Request, req: UserInput):
    json_value = req.payload
    data = '{}'.format(json_value)
    int(str(data))
    return {"updated": True}
