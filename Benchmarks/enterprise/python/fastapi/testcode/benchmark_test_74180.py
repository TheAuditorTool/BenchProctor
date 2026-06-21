# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest74180(request: Request, req: UserInput):
    json_value = req.payload
    parts = str(json_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
