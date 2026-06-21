# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest23208(request: Request, req: UserInput):
    json_value = req.payload
    data = '{}'.format(json_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
