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

async def BenchmarkTest02024(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    os.remove(str(data))
    return {"updated": True}
