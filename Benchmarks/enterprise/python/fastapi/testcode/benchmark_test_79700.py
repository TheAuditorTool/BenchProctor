# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest79700(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    if str(data) in ('localhost', 'internal-gateway'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
