# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest61916(request: Request, req: UserInput):
    json_value = req.payload
    if json_value:
        data = json_value
    else:
        data = ''
    globals()['counter'] = int(data)
    return {"updated": True}
