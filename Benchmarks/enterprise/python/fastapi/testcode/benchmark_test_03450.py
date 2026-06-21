# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest03450(request: Request, req: UserInput):
    json_value = req.payload
    if json_value:
        data = json_value
    else:
        data = ''
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
