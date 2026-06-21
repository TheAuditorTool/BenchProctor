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

async def BenchmarkTest14746(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
