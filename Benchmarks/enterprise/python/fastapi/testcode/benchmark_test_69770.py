# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def to_text(value):
    return str(value).strip()

async def BenchmarkTest69770(request: Request, req: UserInput):
    json_value = req.payload
    data = to_text(json_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
