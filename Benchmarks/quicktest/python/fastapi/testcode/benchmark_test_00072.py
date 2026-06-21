# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest00072(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
