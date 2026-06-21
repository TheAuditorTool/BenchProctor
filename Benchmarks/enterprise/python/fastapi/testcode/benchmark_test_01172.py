# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
def to_text(value):
    return str(value).strip()

async def BenchmarkTest01172(request: Request, req: UserInput):
    json_value = req.payload
    data = to_text(json_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
