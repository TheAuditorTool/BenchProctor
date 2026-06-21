# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
import tempfile


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest05770(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
