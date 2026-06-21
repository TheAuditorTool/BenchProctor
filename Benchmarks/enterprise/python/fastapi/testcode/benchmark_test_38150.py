# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import tempfile


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest38150(request: Request, req: UserInput):
    json_value = req.payload
    pending = list(str(json_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
