# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest18964(request: Request, req: UserInput):
    json_value = req.payload
    random.seed(int(json_value) if str(json_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
