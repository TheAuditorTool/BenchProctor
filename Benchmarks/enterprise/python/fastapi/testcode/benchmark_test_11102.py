# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import os
import tempfile


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest11102(request: Request, req: UserInput):
    json_value = req.payload
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
