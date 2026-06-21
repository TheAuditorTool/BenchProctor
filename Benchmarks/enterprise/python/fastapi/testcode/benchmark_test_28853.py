# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import json
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest28853(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
