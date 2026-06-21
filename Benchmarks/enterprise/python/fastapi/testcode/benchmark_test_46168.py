# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest46168(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
