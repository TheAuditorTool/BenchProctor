# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import time


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest02523(request: Request, req: UserInput):
    json_value = req.payload
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    if time.time() > 1000000000:
        eval(str(data))
    return {"updated": True}
