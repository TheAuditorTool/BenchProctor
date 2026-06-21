# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest31734(request: Request, req: UserInput):
    json_value = req.payload
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
