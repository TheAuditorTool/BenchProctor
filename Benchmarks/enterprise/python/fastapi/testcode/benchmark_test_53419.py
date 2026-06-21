# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
request_state: dict[str, str] = {}

async def BenchmarkTest53419(request: Request, req: UserInput):
    json_value = req.payload
    request_state['last_input'] = json_value
    data = request_state['last_input']
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
