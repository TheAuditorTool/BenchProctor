# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
from starlette.responses import JSONResponse
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest17088(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JSONResponse({'record': str(record)}, status_code=200)
