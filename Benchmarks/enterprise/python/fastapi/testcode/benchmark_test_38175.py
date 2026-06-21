# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest38175(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
