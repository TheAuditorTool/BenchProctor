# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from pydantic import BaseModel
import json
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest70871(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
