# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest22485(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
