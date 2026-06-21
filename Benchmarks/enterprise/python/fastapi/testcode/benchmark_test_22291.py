# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest22291(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
