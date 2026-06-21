# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''
def to_text(value):
    return str(value).strip()

async def BenchmarkTest76520(request: Request, req: UserInput):
    json_value = req.payload
    data = to_text(json_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
