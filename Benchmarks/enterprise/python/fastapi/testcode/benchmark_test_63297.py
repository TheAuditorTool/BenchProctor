# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest63297(request: Request, req: UserInput):
    json_value = req.payload
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(json_value),))
    return JSONResponse({'record': str(record)}, status_code=200)
