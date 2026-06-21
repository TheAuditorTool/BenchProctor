# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest26845(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
