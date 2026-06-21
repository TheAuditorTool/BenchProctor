# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest57135(request: Request, req: UserInput):
    json_value = req.payload
    with open('/var/app/data/' + str(json_value), 'r') as fh:
        content = fh.read()
    return content
