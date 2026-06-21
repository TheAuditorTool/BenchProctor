# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest70046(request: Request, req: UserInput):
    json_value = req.payload
    data = (lambda v: v.strip())(json_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
