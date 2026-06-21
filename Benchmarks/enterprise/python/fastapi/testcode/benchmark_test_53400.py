# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest53400(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
