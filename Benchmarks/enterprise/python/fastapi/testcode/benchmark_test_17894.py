# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest17894(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % (json_value,)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
