# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import tempfile


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest04732(request: Request, req: UserInput):
    json_value = req.payload
    data = (lambda v: v.strip())(json_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
