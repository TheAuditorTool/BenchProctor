# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from dataclasses import dataclass
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest63783(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
