# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest70853(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    request.session['data'] = str(data)
    return {"updated": True}
