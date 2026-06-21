# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest04545(request: Request, req: UserInput):
    json_value = req.payload
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(json_value))
    return {"updated": True}
