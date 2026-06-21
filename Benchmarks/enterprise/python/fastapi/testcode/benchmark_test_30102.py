# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import tempfile


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest30102(request: Request, req: UserInput):
    json_value = req.payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(json_value))
    return {"updated": True}
