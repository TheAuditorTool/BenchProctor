# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest48220(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
