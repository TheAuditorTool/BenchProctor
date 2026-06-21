# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest06092(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
