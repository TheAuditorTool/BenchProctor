# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest23383(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    return HTMLResponse(str(data))
