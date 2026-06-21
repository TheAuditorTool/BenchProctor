# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from pydantic import BaseModel
from starlette.responses import JSONResponse
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest70781(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
