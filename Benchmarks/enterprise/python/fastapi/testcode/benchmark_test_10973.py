# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest10973(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
