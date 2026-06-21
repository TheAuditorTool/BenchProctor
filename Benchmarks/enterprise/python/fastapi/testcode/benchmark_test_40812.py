# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest40812(request: Request, req: UserInput):
    json_value = req.payload
    db.execute('SELECT * FROM users WHERE id = :id', {'id': json_value})
    return {"updated": True}
