# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest29405(request: Request, req: UserInput):
    json_value = req.payload
    data = default_blank(json_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
